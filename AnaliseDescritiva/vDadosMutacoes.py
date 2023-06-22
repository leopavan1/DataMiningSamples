import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    names = ['Grade', 'Gender', 'Age_at_diagnosis', 'Race', 'IDH1', 'TP53', 'ATRX', 'PTEN', 'EGFR', 'CIC', 'MUC16',
             'PIK3CA', 'NF1', 'PIK3R1', 'FUBP1', 'RB1', 'NOTCH1', 'BCOR', 'CSMD3', 'SMARCA4', 'GRIN2A', 'IDH2', 'FAT4',
             'PDGFRA']
    input_file = '0-Datasets/TCGA_GBM_LGG_Mutations_all_Clear.csv'
    df = pd.read_csv(input_file, names=names)

    atributos = ['IDH1', 'TP53', 'ATRX', 'PTEN', 'EGFR', 'CIC', 'MUC16',
                 'PIK3CA', 'NF1', 'PIK3R1', 'FUBP1', 'RB1', 'NOTCH1', 'BCOR', 'CSMD3', 'SMARCA4', 'GRIN2A', 'IDH2',
                 'FAT4', 'PDGFRA']

    plt.figure(figsize=(12, 8))

    # Definir uma lista de cores para os atributos
    cores = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'teal', 'gold', 'navy',
             'darkgreen', 'salmon', 'sienna', 'lime']

    # Gerar o gráfico de barras para cada atributo
    for i, atributo in enumerate(atributos):
        grade_counts = df['Grade'].value_counts()
        attribute_counts = df.groupby('Grade')[atributo].value_counts()
        categories = attribute_counts.index.levels[1]
        attribute_counts_by_grade = attribute_counts.unstack().loc[grade_counts.index, categories].fillna(0)
        
        # Adicionar um pequeno deslocamento horizontal
        offset = i * 0.02
        plt.bar(np.arange(len(categories)) + offset, attribute_counts_by_grade.sum(axis=0), width=0.1, label=atributo, color=cores[i])

    plt.title('Contagem de mutações apresentada por grade')
    plt.xlabel('Grade')
    plt.ylabel('Contagem')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xticks(np.arange(len(categories)), categories, rotation=30)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
