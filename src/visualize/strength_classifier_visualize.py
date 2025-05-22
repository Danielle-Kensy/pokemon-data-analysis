import matplotlib.pyplot as plt
import seaborn as sns


def plot_pokemon_resistance_extremes(df, save_path=None):
    # filtrando colunas de resistência
    resistance_cols = [col for col in df.columns if col.startswith("against_")]

    # calculando a média de resistência
    df["avg_resistance"] = df[resistance_cols].mean(axis=1)

    #top 10 mais resistentes
    top_resistant = df.nlargest(10, "avg_resistance")[
        ["name", "avg_resistance"]].sort_values("avg_resistance")

    #top 10 mais vulneráveis
    top_vulnerable = df.nsmallest(10, "avg_resistance")[
        ["name", "avg_resistance"]].sort_values("avg_resistance")

    # gráfico - pokémons mais resistentes
    plt.figure(figsize=(10, 5))
    sns.barplot(x="avg_resistance", y="name",
                data=top_resistant, palette="Greens_r")
    plt.title("Top 10 Pokémons Mais Resistentes (média de resistências)")
    plt.xlabel("Média de Resistência")
    plt.ylabel("Nome do Pokémon")
    plt.tight_layout()
    # Salvar como PNG se o caminho for fornecido
    if save_path:
        plt.savefig(save_path, format='png', dpi=300)
    plt.show()

    # gráfico - pokémons mais vulneráveis
    plt.figure(figsize=(10, 5))
    sns.barplot(x="avg_resistance", y="name",
                data=top_vulnerable, palette="Reds")
    plt.title("Top 10 Pokémons Mais Vulneráveis (média de resistências)")
    plt.xlabel("Média de Resistência")
    plt.ylabel("Nome do Pokémon")
    plt.tight_layout()
    # Salvar como PNG se o caminho for fornecido
    if save_path:
        plt.savefig(save_path, format='png', dpi=300)
    plt.show()
