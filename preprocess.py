import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def load_and_clean_data(file_path="data/TN.csv"):
    df = pd.read_csv(file_path)

    # Convert Date to datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Drop duplicates and rows with null Taluks
    df.drop_duplicates(inplace=True)
    df = df[df['Taluk'].notnull()]

    # List of required columns
    required_columns = [
        'Population', 'Density', 'Vaccination Rate', 'Hospital Capacity', 'ICU Beds',
        'Ventilators', 'Daily Tests', 'Avg Income', 'Below Poverty Line',
        'Air Quality Index', 'Temperature', 'Humidity', 'Rainfall',
        'Waterborne Cases', 'Income', 'Poverty Rate',
        'Cases', 'Recoveries', 'Deaths', 'R0'
    ]

    # Fill or generate missing columns
    for col in required_columns:
        if col not in df.columns:
            print(f"[INFO] Generating synthetic data for missing column: {col}")
            if col in ['Population']:
                df[col] = np.random.randint(20000, 1500000, size=len(df))
            elif col in ['Density']:
                df[col] = np.random.randint(100, 5000, size=len(df))
            elif col in ['Vaccination Rate']:
                df[col] = np.random.uniform(30, 95, size=len(df))
            elif col in ['Hospital Capacity', 'ICU Beds', 'Ventilators']:
                df[col] = np.random.randint(10, 1000, size=len(df))
            elif col in ['Temperature']:
                df[col] = np.random.uniform(24, 38, size=len(df))
            elif col in ['Humidity']:
                df[col] = np.random.uniform(30, 90, size=len(df))
            elif col in ['Rainfall']:
                df[col] = np.random.uniform(0, 400, size=len(df))
            elif col in ['Air Quality Index']:
                df[col] = np.random.uniform(50, 200, size=len(df))
            elif col in ['Waterborne Cases']:
                df[col] = np.random.randint(0, 100, size=len(df))
            elif col in ['Income']:
                df[col] = np.random.randint(10000, 80000, size=len(df))
            elif col in ['Poverty Rate', 'Below Poverty Line']:
                df[col] = np.random.uniform(5, 40, size=len(df))
            elif col in ['Cases']:
                df[col] = np.random.randint(10, 1000, size=len(df))
            elif col in ['Recoveries']:
                df[col] = df['Cases'] - np.random.randint(0, 100, size=len(df))
            elif col in ['Deaths']:
                df[col] = np.random.randint(0, 50, size=len(df))
            elif col in ['R0']:
                df[col] = np.random.uniform(0.8, 3.5, size=len(df))
            elif col in ['Daily Tests']:
                df[col] = np.random.randint(100, 5000, size=len(df))
            elif col in ['Avg Income']:
                df[col] = np.random.randint(8000, 70000, size=len(df))

    # Replace any negative values generated (e.g., Recoveries) with minimum 0
    numeric_cols_only = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols_only] = df[numeric_cols_only].clip(lower=0)

    # Derived feature: Mobility Index
    df['Mobility Index'] = df['Density'] * (1 - df['Vaccination Rate'] / 100)

    # Normalize selected numerical columns
    numeric_cols = [
        'Population', 'Density', 'Vaccination Rate', 'Hospital Capacity', 'ICU Beds',
        'Ventilators', 'Daily Tests', 'Avg Income', 'Below Poverty Line',
        'Air Quality Index', 'Temperature', 'Humidity', 'Rainfall',
        'Waterborne Cases', 'Income', 'Poverty Rate', 'Mobility Index'
    ]
    numeric_cols = [col for col in numeric_cols if col in df.columns]

    scaler = MinMaxScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df
