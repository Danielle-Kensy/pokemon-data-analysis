import seaborn as sns
import matplotlib.pyplot as plt


def plot_capture_difficulty_by_type(df, save_path=None):
    #garantindo coluna capture_difficulty foi criada
    def categorize_capture_rate(rate):
        try:
            rate = int(rate)
            if rate >= 150:
                return 'Fácil'
            elif rate >= 70:
                return 'Média'
            else:
                return 'Difícil'
        except:
            return 'Desconhecido'

    df['capture_difficulty'] = df['capture_rate'].apply(
        categorize_capture_rate)

    # isolando por tipo e dificuldade
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='type1',
                  hue='capture_difficulty', palette='viridis')
    plt.title('Distribuição da Dificuldade de Captura por Tipo Principal (type1)')
    plt.xlabel('Tipo Principal (type1)')
    plt.ylabel('Quantidade de Pokémons')
    plt.xticks(rotation=45)
    plt.legend(title='Dificuldade de Captura')
    plt.tight_layout()

    # Salvar como PNG se o caminho for fornecido
    if save_path:
        plt.savefig(save_path, format='png', dpi=300)

    plt.show()
