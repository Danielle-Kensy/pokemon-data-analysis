import matplotlib.pyplot as plt

def primary_type_pie_chart(df, save_path):
    tipo_counts = df['type1'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(tipo_counts, labels=tipo_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title("Distribuição dos Tipos Primários")
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()