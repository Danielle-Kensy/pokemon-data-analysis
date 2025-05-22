import matplotlib.pyplot as plt

def plot_most_common_main_type_pie(df, save_path=None):
    grouped = df.groupby(['generation', 'type1']).size().reset_index(name='quantity')
    common_types = grouped.loc[grouped.groupby('generation')['quantity'].idxmax()]
    
    # contando quantas vezes cada tipo aparece como "mais comum" entre as gen
    type_counts = common_types['type1'].value_counts()

    # gráfico de pizza
    plt.figure(figsize=(8, 8))
    plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title("Tipos mais comuns por geração (Distribuição de frequência)")
    plt.axis('equal')  # deixa redondinho

    if save_path:
        plt.savefig(save_path, dpi=300)

    plt.show()