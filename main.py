from src.data_cleaning import load_data, clean_pokemon_data

df_raw = load_data("data/raw/Pokemon.csv")
df_clean = clean_pokemon_data(df_raw)
df_clean.to_csv("data/processed/Pokemon_cleaned.csv", index=False)

print("✅ PokeDados limpinhos com sucesso!")