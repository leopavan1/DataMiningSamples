import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def main():
    names = ['Grade', 'Gender', 'Age_at_diagnosis', 'Race', 'IDH1', 'TP53', 'ATRX', 'PTEN', 'EGFR', 'CIC', 'MUC16', 'PIK3CA', 'NF1', 'PIK3R1', 'FUBP1', 'RB1', 'NOTCH1', 'BCOR', 'CSMD3', 'SMARCA4', 'GRIN2A', 'IDH2', 'FAT4', 'PDGFRA']
    input_file = '0-Datasets/TCGA_GBM_LGG_Mutations_all_Clear.csv'
    df = pd.read_csv(input_file, names=names)
    
    sns.set(style='whitegrid')
    sns.scatterplot(x='Age_at_diagnosis',
                    y='Grade',
                    size='Gender',
                    data=df)
    plt.show()

if __name__ == "__main__":
    main()
