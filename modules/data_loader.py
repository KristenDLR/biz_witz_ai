import pandas as pd

def load_and_clean(filepath):
    print(f"Loading file: {filepath}")
    df = pd.read_csv(filepath)

    # Standardize column names
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    print("Columns after cleaning:", df.columns.tolist())

    # Validate required column
    if 'sales' not in df.columns:
        raise ValueError(f"Expected column 'sales' not found. Available columns: {df.columns.tolist()}")

    # Drop rows with missing sales values
    df.dropna(subset=['sales'], inplace=True)
    print(f"Cleaned data: {df.shape[0]} rows remaining")

    return df
