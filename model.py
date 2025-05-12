import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from preprocess import load_and_clean_data

def train_model():
    print("Loading and preprocessing data...")
    df = load_and_clean_data()

    # Define the final consistent feature set
    features = ['Population', 'Density', 'Vaccination Rate', 'Hospital Capacity', 'ICU Beds', 'Mobility Index', 'Cases','R0']
    missing_features = [col for col in features if col not in df.columns]

    if missing_features:
        print(f"Error: Missing columns {missing_features} in dataset.")
        return

    print("Splitting dataset...")
    X = df[features]
    y = df['Cases'].apply(lambda x: 1 if x > df['Cases'].median() else 0)  # Binary classification

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Training model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    print("Model Evaluation:\n", classification_report(y_test, predictions))

    # Save model
    model_path = "hotspot_model.pkl"
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model()
