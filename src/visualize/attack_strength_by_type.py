import matplotlib.pyplot as plt
import seaborn as sns

def plot_avg_attack_by_type(df):
    # Agrupar por tipo primário e calcular a média de ataque
    attack_means = df.groupby("type1")["attack"].mean().sort_values(ascending=True)

    # Gráfico
    plt.figure(figsize=(12, 6))
    sns.barplot(x=attack_means.values, y=attack_means.index, palette="coolwarm")
    plt.title("Média de Ataque por Tipo Primário de Pokémon")
    plt.xlabel("Média de Ataque")
    plt.ylabel("Tipo Primário")
    plt.tight_layout()
    plt.show()