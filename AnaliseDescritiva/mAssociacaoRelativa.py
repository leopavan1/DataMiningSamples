import matplotlib.pyplot as plt
import pandas as pd

def plot_heatmap(data, title):
    plt.figure(figsize=(10, 10))
    plt.title(title, fontsize=16)
    plt.imshow(data, cmap='coolwarm', interpolation='nearest')
    plt.colorbar(label='Value', pad=0.02)
    plt.xticks(range(len(data.columns)), data.columns, rotation=15, fontsize=10, ha='right')
    plt.yticks(range(len(data.columns)), data.columns, fontsize=10)
    
    # Adiciona os números aos quadrados do heatmap
    for i in range(len(data.columns)):
        for j in range(len(data.columns)):
            plt.text(j, i, "{:.1f}".format(data.iloc[i, j]), ha='center', va='center', color='w', fontsize=8)
    
    plt.tight_layout()
    plt.show()

def main():
    names = ['Grade', 'Gender', 'Age_at_diagnosis', 'Race', 'IDH1', 'TP53', 'ATRX', 'PTEN', 'EGFR', 'CIC', 'MUC16', 'PIK3CA', 'NF1', 'PIK3R1', 'FUBP1', 'RB1', 'NOTCH1', 'BCOR', 'CSMD3', 'SMARCA4', 'GRIN2A', 'IDH2', 'FAT4', 'PDGFRA']
    input_file = '0-Datasets/TCGA_GBM_LGG_Mutations_all_Clear.csv'
    df = pd.read_csv(input_file, names=names)

    # Remover alguns atributos
    attributes_to_remove = [ 'MUC16', 'PIK3CA', 'NF1', 'PIK3R1', 'RB1', 'NOTCH1', 'BCOR', 'CSMD3', 'SMARCA4', 'GRIN2A', 'IDH2', 'FAT4', 'PDGFRA']
    df_filtered = df.drop(columns=attributes_to_remove)

    print("\nMedidas de Associação\n")
    print('Covariância:\n{}'.format(df_filtered.cov()))  # Covariância
    plot_heatmap(df_filtered.cov(), "Matriz de Covariância (Atributos Removidos)")

    print('\nCorrelação:\n{}'.format(df_filtered.corr()))  # Correlação
    plot_heatmap(df_filtered.corr(), "Matriz de Correlação (Atributos Removidos)")

if __name__ == "__main__":
    main()
