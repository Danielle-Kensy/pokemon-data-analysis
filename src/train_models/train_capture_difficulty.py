import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

def categorize_capture_rate(rate):
    if rate >= 150:
        return 'fácil'
    elif rate >= 75:
        return 'médio'
    else:
        return 'difícil'

def train_capture_difficulty_classifier(df):
    # Remover valores ausentes
    df = df.dropna(subset=['capture_rate', 'type1'])

    # Converter capture_rate para numérico
    df['capture_rate'] = pd.to_numeric(df['capture_rate'], errors='coerce')

    # Reaplicar filtro para capturar valores inválidos convertidos em NaN
    df = df.dropna(subset=['capture_rate'])

    # Categoriza capture_rate
    df['capture_difficulty'] = df['capture_rate'].apply(categorize_capture_rate)

    # Codifica tipo principal
    le_type = LabelEncoder()
    df['type1_encoded'] = le_type.fit_transform(df['type1'])

    X = df[['type1_encoded']]
    y = df['capture_difficulty']

    # Divide dados
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Modelo de árvore de decisão
    clf = DecisionTreeClassifier(max_depth=4, random_state=42)
    clf.fit(X_train, y_train)

    # Avaliação
    y_pred = clf.predict(X_test)

    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))

    print("\n📊Relatório de Classificação para dificuldade de captura:")
    print(classification_report(y_test, y_pred))

    return clf, le_type