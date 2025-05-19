import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix

def train_type_classifier(df):
    # Seleciona colunas de atributos de combate
    features = [
        'attack', 'defense', 'sp_attack', 'sp_defense', 'hp',
        'speed', 'base_total', 'experience_growth'
    ]
    
    # Remove linhas com dados ausentes
    df = df.dropna(subset=features + ['type1'])

    # Entrada e saída
    X = df[features]
    y = df['type1']

    # Converte os rótulos para valores numéricos
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    # Divide em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
    )

    # Cria e treina o modelo
    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)

    # Avaliação
    y_pred = clf.predict(X_test)

    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))

    print("\nRelatório de Classificação:")
    print(classification_report(y_test, y_pred, target_names=le.classes_))

    # Importância das features
    feature_importances = pd.Series(clf.feature_importances_, index=X.columns)
    return clf, feature_importances.sort_values(ascending=False), le
