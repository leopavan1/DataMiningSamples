from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.tree import DecisionTreeClassifier, plot_tree
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import numpy as np
import itertools

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.figure()
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')  

def main():
    input_file = '0-Datasets/TCGA_GBM_LGG_Mutations_Balanced.csv'
    names = ['Grade','Gender','Age_at_diagnosis','Race','IDH1','TP53','ATRX','PTEN','EGFR','CIC','MUC16','PIK3CA','NF1','PIK3R1','FUBP1','RB1','NOTCH1','BCOR','CSMD3','SMARCA4','GRIN2A','IDH2','FAT4','PDGFRA'] 
    features = ['Grade','Gender','Age_at_diagnosis','Race','IDH1','TP53','ATRX','PTEN','EGFR','CIC','MUC16','PIK3CA','NF1','PIK3R1','FUBP1','RB1','NOTCH1','BCOR','CSMD3','SMARCA4','GRIN2A','IDH2','FAT4','PDGFRA']
    target = 'Grade'
    df = pd.read_csv(input_file, names=names, usecols=features, na_values=['--', 'not reported'])
                   
    # Separating out the features
    X = df.loc[:, features].values

    # Separating out the target
    y = df.loc[:,[target]].values

    # Standardizing the features
    X = StandardScaler().fit_transform(X)
    normalizedDf = pd.DataFrame(data=X, columns=features)
    normalizedDf = pd.concat([normalizedDf, df[[target]]], axis=1)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    clf = DecisionTreeClassifier(max_leaf_nodes=10)
    clf.fit(X_train, y_train)
    
    predictions = clf.predict(X_test)
    
    # Cálculo da matriz de confusão
    cm = confusion_matrix(y_test, predictions)
    print('Confusion Matrix:')
    print(cm)
    
    # Plotar matriz de confusão
    plot_confusion_matrix(cm, df['Grade'].unique(), False, "Confusion Matrix - Decision Tree")      
    plot_confusion_matrix(cm, df['Grade'].unique(), True, "Confusion Matrix - Decision Tree normalized" )  

    # Cálculo das métricas
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, average='weighted')
    recall = recall_score(y_test, predictions, average='weighted')
    f1 = f1_score(y_test, predictions, average='weighted')
    
    print('Accuracy:', accuracy)
    print('Precision:', precision)
    print('Recall:', recall)
    print('F1-score:', f1)
    
    # Perform cross-validation
    predictions_cv = cross_val_predict(clf, X, y, cv=5)

    # Cálculo da matriz de confusão para cada iteração da validação cruzada
    cm_cv = confusion_matrix(y, predictions_cv)
    print('Confusion Matrix - Cross-Validation:')
    print(cm_cv)

    # Cálculo das métricas para cada iteração da validação cruzada
    accuracy_cv = accuracy_score(y, predictions_cv)
    precision_cv = precision_score(y, predictions_cv, average='weighted')
    recall_cv = recall_score(y, predictions_cv, average='weighted')
    f1_cv = f1_score(y, predictions_cv, average='weighted')

    # Print cross-validation scores
    print('Cross-Validation Accuracy:', accuracy_cv)
    print('Cross-Validation Precision:', precision_cv)
    print('Cross-Validation Recall:', recall_cv)
    print('Cross-Validation F1-score:', f1_cv)

    # Plot bar chart of cross-validation scores
    plt.figure()
    plt.bar(range(1, 6), [accuracy_cv] * 5)
    plt.xlabel('Fold')
    plt.ylabel('Accuracy')
    plt.title('Cross-Validation Scores')
    plt.show()
    
    plt.figure(figsize=(8, 6))
    plot_tree(clf)
    plt.show()


if __name__ == "__main__":
    main()
