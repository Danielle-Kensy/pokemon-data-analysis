from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

def classify_strength(base_total):
    if base_total >= 600:
        return "forte"
    elif base_total >= 400:
        return "médio"
    else:
        return "fraco"

def train_strength_classifier(df):
    # Verifica colunas de resistência
    resistance_cols = [col for col in df.columns if col.startswith('against_')]

    # Remove linhas com valores ausentes nessas colunas
    df_resist = df.dropna(subset=resistance_cols + ['base_total'])

    # Cria variável target (classe de força)
    df_resist['strength_class'] = df_resist['base_total'].apply(classify_strength)

    X = df_resist[resistance_cols]
    y = df_resist['strength_class']

    # Divide em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Modelo Random Forest
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Avaliação
    y_pred = clf.predict(X_test)

    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))

    print("\n📊Relatório de Classificação para força:")
    print(classification_report(y_test, y_pred))

    return clf, resistance_cols