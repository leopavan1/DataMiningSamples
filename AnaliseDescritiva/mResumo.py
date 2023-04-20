import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
     
def main():
    names = ['Grade','Gender','Age_at_diagnosis','Race','IDH1','TP53','ATRX','PTEN','EGFR','CIC','MUC16','PIK3CA','NF1','PIK3R1','FUBP1','RB1','NOTCH1','BCOR','CSMD3','SMARCA4','GRIN2A','IDH2','FAT4','PDGFRA'] 
    features = ['Grade','Gender','Age_at_diagnosis','Race','IDH1','TP53','ATRX','PTEN','EGFR','CIC','MUC16','PIK3CA','NF1','PIK3R1','FUBP1','RB1','NOTCH1','BCOR','CSMD3','SMARCA4','GRIN2A','IDH2','FAT4','PDGFRA']
    input_file = '0-Datasets/TCGA_InfoWithGrade.csv'
    target = 'IDH1','TP53','ATRX','PTEN','EGFR','CIC','MUC16','PIK3CA','NF1','PIK3R1','FUBP1','RB1','NOTCH1','BCOR','CSMD3','SMARCA4','GRIN2A','IDH2','FAT4','PDGFRA'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                    names = names) # Nome das colunas
    
    atributo = 'Age_at_diagnosis'

    print("Medidas de Tendência Central\n")
    print('Média: {:.2f}'.format(df[atributo].mean())) # Média
    print('Mediana: {:.1f}'.format(df[atributo].median())) # Mediana
    print('Ponto Médio: {:.0f}'.format((df[atributo].max() + df[atributo].min())/2)) # Ponto Médio
    print('Moda: ')
    print(format(df[atributo].mode()))
    #print('Moda: {:.0f}'.format((df[atributo].mode()))) # Moda
    
if __name__ == "__main__":
    main()