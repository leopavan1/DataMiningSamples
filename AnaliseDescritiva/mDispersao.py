import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
     
def main():
    names = ['Grade','Gender','Age_at_diagnosis','Race','IDH1','TP53','ATRX','PTEN','EGFR','CIC','MUC16','PIK3CA','NF1','PIK3R1','FUBP1','RB1','NOTCH1','BCOR','CSMD3','SMARCA4','GRIN2A','IDH2','FAT4','PDGFRA'] 
    features = ['Grade','Gender','Age_at_diagnosis','Race','IDH1','TP53','ATRX','PTEN','EGFR','CIC','MUC16','PIK3CA','NF1','PIK3R1','FUBP1','RB1','NOTCH1','BCOR','CSMD3','SMARCA4','GRIN2A','IDH2','FAT4','PDGFRA']
    input_file = '0-Datasets/TCGA_InfoWithGrade.csv'
    target = 'IDH1','TP53','ATRX','PTEN','EGFR','CIC','MUC16','PIK3CA','NF1','PIK3R1','FUBP1','RB1','NOTCH1','BCOR','CSMD3','SMARCA4','GRIN2A','IDH2','FAT4','PDGFRA'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                    names = names) # Nome das colunas
    
    target = 'Gender'

     # Separating out the features
    x = df.loc[1, :].values
    print(df)
    # Separating out the target
    # atributo = df.loc[:,[target]].values
    
    # atb = df.loc[:,['Grade']].values
    
    # df_dispersao = x
    # print(df)
    # fig = plt.figure()
    # ax = fig.add_axes([0,0,1.5,1.5])
    # graf = sns.load_dataset("df")
    # graf.head()
    
    # ax = sns.scatterplot(data=graf, x=atb, y = atributo)
    # print(ax)
    # plt.show()

    sns.set(style='whitegrid')
    #fmri = sns.load_dataset("fmri")
    #print(fmri)
    sns.scatterplot(x="Age_at_diagnosis",
                        y="Grade",
                        data=df)
    plt.show()
    
if __name__ == "__main__":
    main()