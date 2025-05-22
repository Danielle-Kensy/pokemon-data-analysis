import matplotlib.pyplot as plt
import seaborn as sns

def plot_avg_attack_by_type(df, save_path=None):
    # agrupando por tipo primário e calculando média de ataque
    attack_means = df.groupby("type1")["attack"].mean().sort_values(ascending=True)

    # visualização
    plt.figure(figsize=(12, 6))
    sns.barplot(x=attack_means.values, y=attack_means.index, palette="coolwarm")
    plt.title("Média de Ataque por Tipo Primário de Pokémon")
    plt.xlabel("Média de Ataque")
    plt.ylabel("Tipo Primário")
    plt.tight_layout()

        # Salvar como PNG se o caminho for fornecido
    if save_path:
        plt.savefig(save_path, format='png', dpi=300) 

    plt.show()