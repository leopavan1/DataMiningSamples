import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
     
def main():
    names = ['Grade','Gender','Age_at_diagnosis','Race','IDH1','TP53','ATRX','PTEN','EGFR','CIC','MUC16','PIK3CA','NF1','PIK3R1','FUBP1','RB1','NOTCH1','BCOR','CSMD3','SMARCA4','GRIN2A','IDH2','FAT4','PDGFRA'] 
    features = ['Grade','Gender','Age_at_diagnosis','Race','IDH1','TP53','ATRX','PTEN','EGFR','CIC','MUC16','PIK3CA','NF1','PIK3R1','FUBP1','RB1','NOTCH1','BCOR','CSMD3','SMARCA4','GRIN2A','IDH2','FAT4','PDGFRA']
    input_file = '0-Datasets/TCGA_GBM_LGG_Mutations_all_Clear.csv'
    target = 'Age_at_diagnosis'
    df = pd.read_csv(input_file, names=names)
        
    # Separating out the features
    x = df.loc[:, features].values
    # Separating out the target
    idades = df.loc[:,[target]].values
    print(idades)

    plt.title('Idades de um grupo')
    plt.xlabel('Idade')
    plt.ylabel('Frequência Absoluta')
    plt.hist(idades, 8, rwidth=1, edgecolor = 'black')

    # Definir os valores e rótulos dos intervalos no eixo x
    intervalos = np.linspace(np.min(idades), np.max(idades), 9)
    plt.xticks(intervalos)

    plt.show()

if __name__ == "__main__":
    main()
