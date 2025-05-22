import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def plot_type_distribution_by_generation(df, save_path=None):
    # filtra apenas os tipos relevantes
    types_of_interest = ['fairy', 'steel', 'dragon']
    filtered_df = df[df['type1'].isin(types_of_interest)]

    # conta quantos pokémons de cada tipo existem por gen
    type_counts = filtered_df.groupby(
        ['generation', 'type1']).size().reset_index(name='count')

    plt.figure(figsize=(10, 6))
    sns.barplot(data=type_counts, x='generation',
                y='count', hue='type1', palette='Set2')
    plt.title('Distribuição de Pokémons do tipo Fairy, Steel e Dragon por Geração')
    plt.xlabel('Geração')
    plt.ylabel('Quantidade')
    plt.legend(title='Tipo')
    plt.tight_layout()
    # Salvar como PNG se o caminho for fornecido
    if save_path:
        plt.savefig(save_path, format='png', dpi=300)
    plt.show()


def plot_type_proportion_heatmap(df, save_path=None):
    # tipos alvo
    types_of_interest = ['fairy', 'steel', 'dragon']

    # tabela cruzada com contagem de tipos por gen
    crosstab = pd.crosstab(df['generation'], df['type1'])

    # filtrando apenas os tipos desejados
    crosstab_filtered = crosstab[types_of_interest]

    # calculando proporções por geração
    proportions = crosstab_filtered.div(crosstab.sum(axis=1), axis=0)

    # exibir o heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(proportions, annot=True, fmt=".2f",
                cmap='Purples', linewidths=0.5, linecolor='gray')
    plt.title('Proporção de Pokémon Fairy, Steel e Dragon por Geração')
    plt.xlabel('Tipo')
    plt.ylabel('Geração')
    plt.tight_layout()
    # Salvar como PNG se o caminho for fornecido
    if save_path:
        plt.savefig(save_path, format='png', dpi=300)
    plt.show()
