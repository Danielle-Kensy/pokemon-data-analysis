import seaborn as sns
import matplotlib.pyplot as plt


def plot_legendary_distribution(df, save_path=None):
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='is_legendary', palette='Set2')
    plt.xticks([0, 1], ['Não Lendário', 'Lendário'])
    plt.title('Distribuição de Pokémon Lendários')
    plt.xlabel('É Lendário?')
    plt.ylabel('Quantidade')
    plt.tight_layout()
    # Salvar como PNG se o caminho for fornecido
    if save_path:
        plt.savefig(save_path, format='png', dpi=300)
    plt.show()


def plot_stats_comparison(df, save_path=None):
    plt.figure(figsize=(7, 5))
    sns.boxplot(data=df, x='is_legendary', y='base_total', palette='Set3')
    plt.xticks([0, 1], ['Não Lendário', 'Lendário'])
    plt.title('Comparação de Atributos Totais entre Lendários e Não')
    plt.xlabel('É Lendário?')
    plt.ylabel('Total de Atributos (base_total)')
    plt.tight_layout()
    # Salvar como PNG se o caminho for fornecido
    if save_path:
        plt.savefig(save_path, format='png', dpi=300)
        
    plt.show()
