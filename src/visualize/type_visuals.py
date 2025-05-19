import seaborn as sns
import matplotlib.pyplot as plt

def plot_stats_by_type(df):
    stats = ['attack', 'defense', 'speed', 'sp_attack', 'sp_defense', 'hp']
    
    for stat in stats:
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=df, x='type1', y=stat, palette='tab20', showfliers=False)
        plt.xticks(rotation=45)
        plt.title(f'{stat.capitalize()} por Tipo Principal (type1)')
        plt.xlabel('Tipo Principal')
        plt.ylabel(stat.capitalize())
        plt.tight_layout()
        plt.show()
