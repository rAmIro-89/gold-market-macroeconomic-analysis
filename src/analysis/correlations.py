# Correlation utilities
import pandas as pd

def compute_correlations(df: pd.DataFrame, target: str, exclude=None):
    if exclude is None:
        exclude = []
    cols = [c for c in df.columns if c != target and c not in exclude]
    corrs = {}
    for c in cols:
        try:
            corrs[c] = df[target].corr(df[c])
        except Exception:
            pass
    return pd.Series(corrs).sort_values(ascending=False)
