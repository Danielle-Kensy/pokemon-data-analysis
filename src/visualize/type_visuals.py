import seaborn as sns
import matplotlib.pyplot as plt
import os


def plot_stats_by_type(df, save_path=None):
    stats = ['attack', 'defense', 'speed', 'sp_attack', 'sp_defense', 'hp']

    for stat in stats:
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=df, x='type1', y=stat,
                    palette='tab20', showfliers=False)
        plt.xticks(rotation=45)
        plt.title(f'{stat.capitalize()} por Tipo Principal (type1)')
        plt.xlabel('Tipo Principal')
        plt.ylabel(stat.capitalize())
        plt.tight_layout()
        # Salvar como PNG se o caminho for fornecido
        if save_path:
            filename = f"{stat}_por_tipo.png"
            full_path = os.path.join(save_path, filename)
            plt.savefig(full_path, format='png', dpi=300)

    plt.show()
