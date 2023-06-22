import pandas as pd
import numpy as np
import math
from imblearn.under_sampling import RandomUnderSampler

def main():
    # Faz a leitura do arquivo
    names = ['Grade', 'Gender', 'Age_at_diagnosis', 'Race', 'IDH1', 'TP53', 'ATRX', 'PTEN', 'EGFR', 'CIC', 'MUC16', 'PIK3CA', 'NF1', 'PIK3R1', 'FUBP1', 'RB1', 'NOTCH1', 'BCOR', 'CSMD3', 'SMARCA4', 'GRIN2A', 'IDH2', 'FAT4', 'PDGFRA']
    features = ['Grade', 'Gender', 'Age_at_diagnosis', 'Race', 'IDH1', 'TP53', 'ATRX', 'PTEN', 'EGFR', 'CIC', 'MUC16', 'PIK3CA', 'NF1', 'PIK3R1', 'FUBP1', 'RB1', 'NOTCH1', 'BCOR', 'CSMD3', 'SMARCA4', 'GRIN2A', 'IDH2', 'FAT4', 'PDGFRA']
    output_file = '0-Datasets/TCGA_GBM_LGG_Mutations_Balanced.csv'
    input_file = '0-Datasets/TCGA_GBM_LGG_Mutations_all_Clear.csv'
    df = pd.read_csv(input_file, names=names, usecols=features, na_values=['--', 'not reported'])
    
    df_original = df.copy()
    
    # Adiciona uma coluna de índices
    df['Index'] = np.arange(len(df))
    
    # Balanceamento dos dados
    undersampler = RandomUnderSampler(random_state=0)
    X_resampled, y_resampled = undersampler.fit_resample(df.drop('Grade', axis=1), df['Grade'])
    
    # Obtém os índices dos dados balanceados
    unique_counts = pd.Series(y_resampled).value_counts()
    resampled_indices = []
    for grade, count in unique_counts.items():
        grade_indices = np.random.choice(df[df['Grade'] == grade]['Index'], size=count, replace=False)
        resampled_indices.extend(grade_indices)
    resampled_indices = np.sort(resampled_indices)
    
    # Recria o DataFrame balanceado
    balanced_df = pd.concat([pd.DataFrame(X_resampled, columns=df.drop('Grade', axis=1).columns), pd.Series(y_resampled, name='Grade')], axis=1)
    balanced_df['Index'] = resampled_indices
    
    # Reordena os dados pelo índice
    balanced_df.sort_values(by='Index', inplace=True)
    balanced_df.drop('Index', axis=1, inplace=True)
    
    # Move a coluna 'Grade' para o início
    cols = list(balanced_df.columns)
    cols.insert(0, cols.pop(cols.index('Grade')))
    balanced_df = balanced_df[cols]
    
    # Remove a coluna de índices do DataFrame original
    df.drop('Index', axis=1, inplace=True)
    
    # Salva arquivo com o balanceamento
    balanced_df.to_csv(output_file, header=False, index=False)

if __name__ == "__main__":
    main()
