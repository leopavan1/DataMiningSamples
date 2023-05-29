import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
     
def main():
    names = ['Grade','Gender','Age_at_diagnosis','Race','IDH1','TP53','ATRX','PTEN','EGFR','CIC','MUC16','PIK3CA','NF1','PIK3R1','FUBP1','RB1','NOTCH1','BCOR','CSMD3','SMARCA4','GRIN2A','IDH2','FAT4','PDGFRA'] 
    features = ['Grade','Gender','Age_at_diagnosis','Race','IDH1','TP53','ATRX','PTEN','EGFR','CIC','MUC16','PIK3CA','NF1','PIK3R1','FUBP1','RB1','NOTCH1','BCOR','CSMD3','SMARCA4','GRIN2A','IDH2','FAT4','PDGFRA']
    input_file = '0-Datasets/TCGA_GBM_LGG_Mutations_all_Clear.csv'
    target = 'IDH1','TP53','ATRX','PTEN','EGFR','CIC','MUC16','PIK3CA','NF1','PIK3R1','FUBP1','RB1','NOTCH1','BCOR','CSMD3','SMARCA4','GRIN2A','IDH2','FAT4','PDGFRA'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                    names = names) # Nome das colunas
    
    atributo = 'Age_at_diagnosis'

    print("\nMedidas de Posição Relativa\n")
    print('Z Score:\n{}\n'.format((df[atributo] - df[atributo].mean())/df[atributo].std())) # Z Score
    print('Quantil (25%): {}'.format(df[atributo].quantile(q=0.25))) # Quantil 25%
    print('Quantil (50%): {}'.format(df[atributo].quantile(q=0.50))) # Quantil 50%
    print('Quantil (75%): {}'.format(df[atributo].quantile(q=0.75))) # Quantil 75%
    
if __name__ == "__main__":
    main()