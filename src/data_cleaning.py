import pandas as pd

def load_data(path):
    #Carrega os dados do arquivo CSV
    return pd.read_csv(path)

def clean_pokemon_data(df):
     # Corrigi nome de coluna (erro de digitação do criador)
    df.rename(columns={'classfication': 'classification'}, inplace=True)

    # Trata valores ausentes
    df['percentage_male'].fillna(0, inplace=True)
    df['type1'].fillna('None', inplace=True)
    df['type2'].fillna('None', inplace=True)
    df['abilities'] = df['abilities'].apply(lambda x: eval(x) if isinstance(x, str) else x)

    # Remove ou corrigir valores estranhos
    df['height_m'].replace(0, pd.NA, inplace=True)
    df['weight_kg'].replace(0, pd.NA, inplace=True)
    
    # Converte 'is_legendary' para booleano
    df['is_legendary'] = df['is_legendary'].astype(bool)
    
    # Limpar colunas de tipo "against_?"
    for column in df.columns:
        if column.startswith('against_'):
            df[column].fillna(0, inplace=True)

    # Remover duplicados
    df.drop_duplicates(subset=['pokedex_number'], inplace=True)

    return df