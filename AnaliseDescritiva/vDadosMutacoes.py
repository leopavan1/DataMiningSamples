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
        
    # Mostrando o número de LGG e de GBM


    label = ['IDH1','TP53','ATRX','PTEN','EGFR','CIC','MUC16','PIK3CA','NF1','PIK3R1','FUBP1','RB1','NOTCH1','BCOR','CSMD3','SMARCA4','GRIN2A','IDH2','FAT4','PDGFRA']

    IDH1 = df['IDH1'].value_counts()[1]
    TP53 = df['TP53'].value_counts()[1]
    ATRX = df['ATRX'].value_counts()[1]
    PTEN = df['PTEN'].value_counts()[1]
    EGFR = df['EGFR'].value_counts()[1]
    CIC = df['CIC'].value_counts()[1]
    MUC16 = df['MUC16'].value_counts()[1]
    PIK3CA = df['PIK3CA'].value_counts()[1]
    NF1 = df['NF1'].value_counts()[1]
    PIK3R1 = df['PIK3R1'].value_counts()[1]
    FUBP1 = df['FUBP1'].value_counts()[1]
    RB1 = df['RB1'].value_counts()[1]
    NOTCH1 = df['NOTCH1'].value_counts()[1]
    BCOR = df['BCOR'].value_counts()[1]
    CSMD3 = df['CSMD3'].value_counts()[1]
    SMARCA4 = df['SMARCA4'].value_counts()[1]
    GRIN2A = df['GRIN2A'].value_counts()[1]
    IDH2 = df['IDH2'].value_counts()[1]
    FAT4 = df['FAT4'].value_counts()[1]
    PDGFRA = df['PDGFRA'].value_counts()[1]
    total = IDH1 + TP53 + ATRX + PTEN + EGFR + CIC + MUC16 + PIK3CA + NF1 + PIK3R1 + FUBP1 + RB1 + NOTCH1 + BCOR + CSMD3 + SMARCA4 + GRIN2A + IDH2 + FAT4 + PDGFRA
    y = np.array([IDH1, TP53, ATRX, PTEN, EGFR, CIC, MUC16, PIK3CA, NF1, PIK3R1, FUBP1, RB1, NOTCH1, BCOR, CSMD3, SMARCA4, GRIN2A, IDH2, FAT4, PDGFRA])
    plt.pie(y , labels=label, autopct= lambda x: '{:.0f}'.format(x*y.sum()/100, startangle=0))
    plt.title('Glioma')
    plt.show() 
    print("Total: {}\n".format(total) )
    print("IDH1: {:.2f}%\n".format((IDH1*100)/total))
    print("TP53: {:.2f}%\n".format((TP53*100)/total))
    print("ATRX: {:.2f}%\n".format((ATRX*100)/total))
    print("PTEN: {:.2f}%\n".format((PTEN*100)/total))
    print("EGFR: {:.2f}%\n".format((EGFR*100)/total))
    print("CIC: {:.2f}%\n".format((CIC*100)/total))
    print("MUC16: {:.2f}%\n".format((MUC16*100)/total))
    print("PIK3CA: {:.2f}%\n".format((PIK3CA*100)/total))
    print("NF1: {:.2f}%\n".format((NF1*100)/total))
    print("PIK3R1: {:.2f}%\n".format((PIK3R1*100)/total))
    print("FUBP1: {:.2f}%\n".format((FUBP1*100)/total))
    print("RB1: {:.2f}%\n".format((RB1*100)/total))
    print("NOTCH1: {:.2f}%\n".format((NOTCH1*100)/total))
    print("BCOR: {:.2f}%\n".format((BCOR*100)/total))
    print("CSMD3: {:.2f}%\n".format((CSMD3*100)/total))
    print("SMARCA4: {:.2f}%\n".format((SMARCA4*100)/total))
    print("GRIN2A: {:.2f}%\n".format((GRIN2A*100)/total))
    print("IDH2: {:.2f}%\n".format((IDH2*100)/total))
    print("FAT4: {:.2f}%\n".format((FAT4*100)/total))
    print("PDGFRA: {:.2f}%\n".format((PDGFRA*100)/total))

if __name__ == "__main__":
    main()