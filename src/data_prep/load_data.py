# Load raw gold and macro datasets
# This script centralizes file path references for reuse in notebooks.
import pandas as pd
from pathlib import Path

RAW_DIR = Path(__file__).resolve().parents[2] / 'data' / 'raw'
PROCESSED_DIR = Path(__file__).resolve().parents[2] / 'data' / 'processed'

GOLD_LONGTERM_FILE = RAW_DIR / 'gold_longterm_drivers.xlsx'

def load_gold_longterm():
    return pd.read_excel(GOLD_LONGTERM_FILE)

if __name__ == '__main__':
    df = load_gold_longterm()
    print(df.head())
