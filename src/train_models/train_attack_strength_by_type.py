import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

def categorize_attack(attack_value):
    if attack_value >= 120:
        return "muito forte"
    elif attack_value >= 80:
        return "médio"
    else:
        return "fraco"

def train_attack_strength_by_type(df):
    # Remove valores ausentes
    df = df.dropna(subset=['attack', 'type1'])

    # Categoriza os ataques
    df['attack_class'] = df['attack'].apply(categorize_attack)

    # Codifica o tipo para número
    le_type = LabelEncoder()
    df['type1_encoded'] = le_type.fit_transform(df['type1'])

    X = df[['type1_encoded']]
    y = df['attack_class']

    # Divide em treino e teste
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

    print("\n📊Relatório de Classificação de ataque baseado no tipo:")
    print(classification_report(y_test, y_pred))

    return clf, le_type