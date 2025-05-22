from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


def plot_generation_confusion_matrix(modelo, X_test, y_test, save_path=None):
    # pervisão
    y_pred = modelo.predict(X_test)

    # gerando matriz
    cm = confusion_matrix(y_test, y_pred, labels=sorted(y_test.unique()))

    # gerando heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='YlGnBu',
                xticklabels=sorted(y_test.unique()),
                yticklabels=sorted(y_test.unique()))
    plt.xlabel('Geração Prevista')
    plt.ylabel('Geração Real')
    plt.title('Matriz de Confusão - Previsão da Geração')
    plt.tight_layout()

    # Salvar como PNG se o caminho for fornecido
    if save_path:
        plt.savefig(save_path, format='png', dpi=300)

    plt.show()
