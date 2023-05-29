import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
     
def main():
    names = ['Grade','Gender','Age_at_diagnosis','Race','IDH1','TP53','ATRX','PTEN','EGFR','CIC','MUC16','PIK3CA','NF1','PIK3R1','FUBP1','RB1','NOTCH1','BCOR','CSMD3','SMARCA4','GRIN2A','IDH2','FAT4','PDGFRA'] 
    features = ['Grade','Gender','Age_at_diagnosis','Race','IDH1','TP53','ATRX','PTEN','EGFR','CIC','MUC16','PIK3CA','NF1','PIK3R1','FUBP1','RB1','NOTCH1','BCOR','CSMD3','SMARCA4','GRIN2A','IDH2','FAT4','PDGFRA']
    input_file = '0-Datasets/TCGA_GBM_LGG_Mutations_all_Clear.csv'
    target = 'Gender'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                    names = names) # Nome das colunas
        
    # Mostrando o número de Masculino e de Feminino


    label = ['Masculino','Feminino']
    cores = ['r','b']
    Masculino = df['Gender'].value_counts()[0]
    Feminino = df['Gender'].value_counts()[1]
    total = Masculino + Feminino
    y = np.array([Masculino, Feminino])
    plt.pie(y , labels=label, colors=cores, autopct= lambda x: '{:.0f}'.format(x*y.sum()/100, startangle=90))
    plt.title('Glioma')
    plt.show() 
    print("Total: {}\n".format(total) )
    print("Masculino: {:.2f}%\n".format((Masculino*100)/total))
    print("Feminino: {:.2f}%\n".format((Feminino*100)/total))

if __name__ == "__main__":
    main()