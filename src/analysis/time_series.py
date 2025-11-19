# Time series helper functions for gold macro analysis
import pandas as pd

def quarterly_summary(df: pd.DataFrame, date_col: str):
    out = df.copy()
    out[date_col] = pd.to_datetime(out[date_col])
    out = out.set_index(date_col).resample('Q').mean().reset_index()
    return out
