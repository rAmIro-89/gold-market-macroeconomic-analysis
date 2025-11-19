# Macro relations scaffolding
# Functions to relate gold metrics with macro indicators (e.g., regression, lag correlation)
import pandas as pd

def lag_correlation(df: pd.DataFrame, col_a: str, col_b: str, max_lag: int = 4):
    results = []
    for lag in range(0, max_lag + 1):
        shifted = df[col_b].shift(lag)
        corr = df[col_a].corr(shifted)
        results.append({'lag': lag, 'correlation': corr})
    return pd.DataFrame(results)
