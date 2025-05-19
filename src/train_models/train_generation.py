import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import MultiLabelBinarizer

def train_generation_classifier(df):
    # Stats e resistências
    stat_cols = ['attack', 'defense', 'hp', 'speed', 'sp_attack', 'sp_defense', 'base_total', 'experience_growth']
    resistance_cols = [col for col in df.columns if col.startswith('against_')]

    # Habilidades: transforma lista de habilidades em colunas (one-hot encoding)
    mlb = MultiLabelBinarizer()
    abilities_encoded = pd.DataFrame(mlb.fit_transform(df['abilities']), columns=mlb.classes_, index=df.index)

    # Junta tudo
    X = pd.concat([df[stat_cols + resistance_cols], abilities_encoded], axis=1)
    y = df['generation']

    # Remove entradas com dados ausentes
    X = X.dropna()
    y = y.loc[X.index]

    # Divisão treino/teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Modelo
    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)

    # Avaliação
    y_pred = clf.predict(X_test)

    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))

    print("\nRelatório de Classificação:")
    print(classification_report(y_test, y_pred))

    # Importância das features
    feature_importances = pd.Series(clf.feature_importances_, index=X.columns)
    return clf, feature_importances.sort_values(ascending=False), X_test, y_test
