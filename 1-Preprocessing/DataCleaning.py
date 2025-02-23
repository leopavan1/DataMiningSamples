import pandas as pd
import numpy as np
import math

def convert_age_to_years(age):
    if isinstance(age, str) and age != 'Age_at_diagnosis':  # Verifica se é uma string e não é o cabeçalho
        parts = age.split()
        if len(parts) == 4:
            years = int(parts[0])
            days = int(parts[2])
            total_years = years + days / 365
            return round(total_years, 2)
        elif len(parts) == 2:
            years = int(parts[0])
            return years
    return math.nan

def main():
    # Faz a leitura do arquivo
    names = ['Grade','Project','Case_ID','Gender','Age_at_diagnosis','Primary_Diagnosis','Race','IDH1','TP53','ATRX','PTEN','EGFR','CIC','MUC16','PIK3CA','NF1','PIK3R1','FUBP1','RB1','NOTCH1','BCOR','CSMD3','SMARCA4','GRIN2A','IDH2','FAT4','PDGFRA'] 
    features = ['Grade','Gender','Age_at_diagnosis','Race','IDH1','TP53','ATRX','PTEN','EGFR','CIC','MUC16','PIK3CA','NF1','PIK3R1','FUBP1','RB1','NOTCH1','BCOR','CSMD3','SMARCA4','GRIN2A','IDH2','FAT4','PDGFRA']
    output_file = '0-Datasets/TCGA_GBM_LGG_Mutations_all_Clear.csv'
    input_file = '0-Datasets/TCGA_GBM_LGG_Mutations_all.csv'
    df = pd.read_csv(input_file,         # Nome do arquivo com dados
                     names = names,      # Nome das colunas 
                     usecols = features, # Define as colunas que serão  utilizadas
                     na_values=['--', 'not reported'])      # Define que ? será considerado valores ausentes
    
    df_original = df.copy()
    # Imprime as 15 primeiras linhas do arquivo
    print("PRIMEIRAS 15 LINHAS\n")
    print(df.head(15))
    print("\n")        

    # Imprime informações sobre dos dados
    print("INFORMAÇÕES GERAIS DOS DADOS\n")
    print(df.info())
    print("\n")
    
    # Imprime uma analise descritiva sobre dos dados
    print("DESCRIÇÃO DOS DADOS\n")
    print(df.describe())
    print("\n")
    
    # Imprime a quantidade de valores faltantes por coluna
    print("VALORES FALTANTES\n")
    print(df.isnull().sum())
    print("\n")    
   
    # Converte dados categóricos em numéricos
    df['Age_at_diagnosis'] = df['Age_at_diagnosis'].apply(convert_age_to_years)
    df['Grade'].replace({'LGG': 0, 'GBM': 1}, inplace=True)
    df['Gender'].replace({'Male': 0, 'Female': 1}, inplace=True)
    df['Race'].replace({'white': 0, 'black or african american': 1, 'asian': 2, 'american indian or alaska native': 3}, inplace=True)
    df['IDH1'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
    df['TP53'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
    df['ATRX'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
    df['PTEN'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
    df['EGFR'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
    df['CIC'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
    df['MUC16'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
    df['PIK3CA'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
    df['NF1'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
    df['PIK3R1'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
    df['FUBP1'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
    df['RB1'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
    df['NOTCH1'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
    df['BCOR'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
    df['CSMD3'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
    df['SMARCA4'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
    df['GRIN2A'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
    df['IDH2'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
    df['FAT4'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
    df['PDGFRA'].replace({'NOT_MUTATED': 0, 'MUTATED': 1}, inplace=True)
       
    columns_missing_value = df.columns[df.isnull().any()]
    print(columns_missing_value)
    method = 'clear' # number ou median ou mean ou mode
    
    for c in columns_missing_value:
        UpdateMissingValues(df, c, method)    

    print(df.describe())
    print("\n")
    print(df.head(15))
    print(df_original.head(15))
    print("\n")
    
    # Salva arquivo com o tratamento para dados faltantes
    df.to_csv(output_file, header=False, index=False)  
    

def UpdateMissingValues(df, column, method="mode", number=0):
    if method == 'number':
        # Substituindo valores ausentes por um número
        df[column].fillna(number, inplace=True)
    elif method == 'median':
        # Substituindo valores ausentes pela mediana 
        median = df[column].median()
        df[column].fillna(median, inplace=True)
    elif method == 'mean':
        # Substituindo valores ausentes pela média
        mean = df[column].mean()
        df[column].fillna(mean, inplace=True)
    elif method == 'mode':
        # Substituindo valores ausentes pela moda
        mode = df[column].mode()[0]
        df[column].fillna(mode, inplace=True)
    elif method == 'clear':
        # Removendo linhas com valores faltantes da coluna especificada
        df.dropna(subset=[column], inplace=True)

if __name__ == "__main__":
    main()