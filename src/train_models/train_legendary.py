import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

def train_legendary_classifier(df):
    # Seleciona as colunas relevantes
    features = [
        'attack', 'defense', 'sp_attack', 'sp_defense', 'speed', 'hp',
        'height_m', 'weight_kg', 'base_total', 'generation', 'experience_growth'
    ] + [col for col in df.columns if col.startswith('against_')]

    # Remove entradas com dados ausentes nas colunas selecionadas
    df = df.dropna(subset=features)

    X = df[features]
    y = df['is_legendary']

    # Divide em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Cria e treina o modelo
    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)

    # Avalia
    y_pred = clf.predict(X_test)
    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))
    print("\nRelatório de Classificação:")
    print(classification_report(y_test, y_pred))

    # Importância das features
    feature_importances = pd.Series(clf.feature_importances_, index=X.columns)
    return clf, feature_importances.sort_values(ascending=False)