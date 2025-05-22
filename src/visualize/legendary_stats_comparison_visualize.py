import matplotlib.pyplot as plt
import pandas as pd

def plot_legendary_stats_comparison(df, save_path=None):
    x_axis = df['is_legendary']
    y_axis = df[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']]
    df_combined = pd.concat([x_axis, y_axis], axis=1)

    # Agrupa os valores baseado no boolean o campo "lendário" e transforma seus valores em Sim e Não para facilitar a visualização
    comparison_table = df_combined.groupby('is_legendary').mean()
    comparison_table.plot(kind='bar', figsize=(10, 6))

    # Gerando o gráfico e suas descrições
    plt.xlabel('É Lendário')
    plt.ylabel('Valor Médio da Característica')
    plt.title('Comparação dos atributos médios entre Pokémon Lendários e Não Lendários')
    plt.xticks(rotation=0)

    if save_path:
        plt.savefig(save_path, format='png', dpi=300)

    plt.show()