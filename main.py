from src.data_cleaning import load_data, clean_pokemon_data

#dashboard📊
from src.generate_dashboard_with_charts import generate_dashboard_with_charts

from src.train_models.train_legendary import train_legendary_classifier
from src.visualize.legendary_visuals import plot_legendary_distribution, plot_stats_comparison

from src.train_models.train_type import train_type_classifier
from src.visualize.type_visuals import plot_stats_by_type

from src.train_models.train_type_by_generation import train_type_focus_classifier
from src.visualize.type_by_generation_visuals import plot_type_distribution_by_generation, plot_type_proportion_heatmap

from src.train_models.train_generation import train_generation_classifier
from src.visualize.generation_visualize import plot_generation_confusion_matrix

from src.train_models.train_capture_difficulty import train_capture_difficulty_classifier
from src.visualize.capture_difficulty_visualize import plot_capture_difficulty_by_type

from src.train_models.train_strength_classifier import train_strength_classifier
from src.visualize.strength_classifier_visualize import plot_pokemon_resistance_extremes

from src.train_models.train_attack_strength_by_type import train_attack_strength_by_type
from src.visualize.attack_strength_by_type import plot_avg_attack_by_type

#Gráficos apenas para visualização sem treino do modelo
from src.visualize.primary_type_visualize import primary_type_pie_chart
from src.visualize.legendary_stats_comparison_visualize import plot_legendary_stats_comparison
from src.visualize.most_common_main_type_pie_visualize import plot_most_common_main_type_pie

# Carregando e limpando os dados
df_raw = load_data("data/raw/Pokemon.csv")
df_clean = clean_pokemon_data(df_raw)
df_clean.to_csv("data/processed/Pokemon_cleaned.csv", index=False)
print("✅ PokeDados limpinhos com sucesso!")

#gerando dashboard final
generate_dashboard_with_charts(graphics_folder="data/graphics/")

# Visualizando a distribuição dos tipos primários
primary_type_pie_chart(df_clean, save_path="data/graphics/0_tipos_primarios.png")
# Comparação gráfica dos atributos base dos pokemons lendários e não lendários
plot_legendary_stats_comparison(df_clean, save_path="data/graphics/1_comparacao_atributos_entre_lendarios_e_nao_grafico.png")
# Gráfico de pizza com a quantidade de tipos mais comuns por geração
plot_most_common_main_type_pie(df_clean, save_path="data/graphics/0.1_tipos_mais_comuns_por_geracao.png")

# Treinando o modelo para prever se é lendário e visualizando
modelo, importancias = train_legendary_classifier(df_clean)
print("\n📊 Importância das features para prever se é lendário:")
print(importancias)
plot_legendary_distribution(df_clean, save_path="data/graphics/1_e_lendario.png")
plot_stats_comparison(df_clean , save_path="data/graphics/1_comparacao_atributos_entre_lendarios_e_nao.png")

# Treinando o modelo para prever o tipo
modelo_type1, importancias_type1, label_encoder_type1 = train_type_classifier(df_clean)
print("\n📊Importância das features para prever o tipo:")
print(importancias_type1)
plot_stats_by_type(df_clean, save_path="data/graphics/")

# Treinando o modelo para prever o tipo de acordo com a geração
modelo_focus, importancias_focus, encoder_focus = train_type_focus_classifier(df_clean)
print("\n📊Importância das features para prever fairy/steel/dragon:")
print(importancias_focus)
plot_type_distribution_by_generation(df_clean, save_path="data/graphics/3_tipo_por_geracao.png")
plot_type_proportion_heatmap(df_clean, save_path="data/graphics/3_tipo_por_geracao_heatmap.png")

# Treinando o modelo para prever a geração com base nos stats
modelo_generation, importancias_generation, X_test_gen, y_test_gen = train_generation_classifier(df_clean)
print("\n📊Importância das features para prever geração:")
print(importancias_generation.head(20))
plot_generation_confusion_matrix(modelo_generation, X_test_gen, y_test_gen, save_path="data/graphics/4_geracao_stats.png")

# Treinando o modelo para prever a dificuldade de captura
modelo_capture, encoder_type1 = train_capture_difficulty_classifier(df_clean)
plot_capture_difficulty_by_type(df_clean, save_path="data/graphics/5_captura_dificuldade.png")

# Treinando o modelo para classificar a força
modelo_strength, resistance_features = train_strength_classifier(df_clean)
plot_pokemon_resistance_extremes(df_clean, save_path="data/graphics/6_força_por_resistencia.png")

# Treinando o modelo para classificar o ataque de acordo com o tipo
modelo_attack, encoder_type = train_attack_strength_by_type(df_clean)
plot_avg_attack_by_type(df_clean, save_path="data/graphics/7_ataque_por_tipo.png")
