
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix

def train_type_focus_classifier(df):
    # Foco nos tipos de interesse
    focus_types = ['fairy', 'steel', 'dragon']

    def label_focus_type(row):
        if row['type1'] in focus_types:
            return row['type1']
        elif row['type2'] in focus_types:
            return row['type2']
        else:
            return 'other'

    df['focus_type'] = df.apply(label_focus_type, axis=1)

    # Filtra apenas Pokémon com tipo definido
    df = df.dropna(subset=['generation', 'attack', 'defense', 'sp_attack', 'sp_defense', 'hp', 'speed'])

    # Features (geração + atributos de combate)
    features = [
        'generation', 'attack', 'defense', 'sp_attack',
        'sp_defense', 'hp', 'speed', 'base_total', 'experience_growth'
    ]
    X = df[features]
    y = df['focus_type']

    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    # Divisão treino/teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
    )

    # Modelo
    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)

    # Avaliação
    y_pred = clf.predict(X_test)

    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))

    print("\nRelatório de Classificação")
    print(classification_report(y_test, y_pred, target_names=le.classes_))

    # Importância das features
    feature_importances = pd.Series(clf.feature_importances_, index=X.columns)
    return clf, feature_importances.sort_values(ascending=False), le