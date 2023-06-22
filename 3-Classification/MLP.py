import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega os dados
input_file = '0-Datasets/TCGA_GBM_LGG_Mutations_Balanced.csv'
names = ['Grade', 'Gender', 'Age_at_diagnosis', 'Race', 'IDH1', 'TP53', 'ATRX', 'PTEN', 'EGFR', 'CIC', 'MUC16', 'PIK3CA', 'NF1', 'PIK3R1', 'FUBP1', 'RB1', 'NOTCH1', 'BCOR', 'CSMD3', 'SMARCA4', 'GRIN2A', 'IDH2', 'FAT4', 'PDGFRA']
features = ['Grade', 'Gender', 'Age_at_diagnosis', 'Race', 'IDH1', 'TP53', 'ATRX', 'PTEN', 'EGFR', 'CIC', 'MUC16', 'PIK3CA', 'NF1', 'PIK3R1', 'FUBP1', 'RB1', 'NOTCH1', 'BCOR', 'CSMD3', 'SMARCA4', 'GRIN2A', 'IDH2', 'FAT4', 'PDGFRA']
target = 'Grade'
df = pd.read_csv(input_file, names=names, usecols=features, na_values=['--', 'not reported'])

# Separa os atributos de entrada e o alvo
X = df[features].values
y = df[target].values

# Divide os dados em conjunto de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Cria o modelo MLP
mlp = MLPClassifier(hidden_layer_sizes=(4, 4, 4), max_iter=500)

# Treina o modelo
mlp.fit(X_train, y_train)

# Realiza previsões no conjunto de teste
y_pred = mlp.predict(X_test)

# Calcula a matriz de confusão
cm = confusion_matrix(y_test, y_pred)

# Calcula a matriz de confusão normalizada
cm_normalized = confusion_matrix(y_test, y_pred, normalize='true')

# Calcula as métricas de avaliação
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print('Acurácia: %.2f' % accuracy)
print('Precisão: %.2f' % precision)
print('Recall: %.2f' % recall)
print('F1-Score: %.2f' % f1)

# Plota a matriz de confusão
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Matriz de Confusão')
plt.xlabel('Rótulo Previsto')
plt.ylabel('Rótulo Real')

# Plota a matriz de confusão normalizada
plt.subplot(1, 2, 2)
sns.heatmap(cm_normalized, annot=True, cmap='Blues')
plt.title('Matriz de Confusão Normalizada')
plt.xlabel('Rótulo Previsto')
plt.ylabel('Rótulo Real')

plt.tight_layout()
plt.show()