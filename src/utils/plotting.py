# Plotting utilities
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')

def line(df, x, y, title=None):
    plt.figure(figsize=(10,4))
    plt.plot(df[x], df[y])
    plt.title(title or f'{y} over {x}')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.tight_layout()
