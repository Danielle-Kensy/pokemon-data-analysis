import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_type_distribution_by_generation(df):
    # Filtrar apenas os tipos relevantes
    types_of_interest = ['fairy', 'steel', 'dragon']
    filtered_df = df[df['type1'].isin(types_of_interest)]

    # Contar quantos pokémons de cada tipo há por geração
    type_counts = filtered_df.groupby(['generation', 'type1']).size().reset_index(name='count')

    plt.figure(figsize=(10, 6))
    sns.barplot(data=type_counts, x='generation', y='count', hue='type1', palette='Set2')
    plt.title('Distribuição de Pokémons do tipo Fairy, Steel e Dragon por Geração')
    plt.xlabel('Geração')
    plt.ylabel('Quantidade')
    plt.legend(title='Tipo')
    plt.tight_layout()
    plt.show()

def plot_type_proportion_heatmap(df):
    # Tipos de interesse
    types_of_interest = ['fairy', 'steel', 'dragon']
    
    # Criar uma tabela cruzada com contagem de tipos por geração
    crosstab = pd.crosstab(df['generation'], df['type1'])

    # Filtrar apenas os tipos desejados
    crosstab_filtered = crosstab[types_of_interest]

    # Calcular proporções por geração
    proportions = crosstab_filtered.div(crosstab.sum(axis=1), axis=0)

    # Plotar heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(proportions, annot=True, fmt=".2f", cmap='Purples', linewidths=0.5, linecolor='gray')
    plt.title('Proporção de Pokémon Fairy, Steel e Dragon por Geração')
    plt.xlabel('Tipo')
    plt.ylabel('Geração')
    plt.tight_layout()
    plt.show()