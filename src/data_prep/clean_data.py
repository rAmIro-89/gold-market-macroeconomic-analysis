# Cleaning utilities for gold macro dataset
import pandas as pd

def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    return df

if __name__ == '__main__':
    from load_data import load_gold_longterm
    raw = load_gold_longterm()
    clean = standardize_columns(raw)
    print(clean.head())
