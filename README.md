# Gold and Power: Macroeconomic Analysis

![Project Status](https://img.shields.io/badge/status-completed-success)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Power BI](https://img.shields.io/badge/PowerBI-Interactive%20Dashboard-yellow)
![Data Sources](https://img.shields.io/badge/Data%20Sources-FRED%20|%20World%20Bank%20|%20WGC%20|%20IMF-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)

A comprehensive data analysis project exploring the relationship between gold prices and global macroeconomic indicators from 2014 to 2024.

## 📊 Project Overview

This project analyzes gold as a global economic indicator by examining its relationship with key macroeconomic variables including USD index, interest rates, inflation, oil prices, equity markets, and geopolitical factors.

**Key Objectives:**
- Build a comprehensive dataset integrating gold prices with macroeconomic indicators
- Analyze correlations and trends between gold and economic variables
- Create interactive visualizations to communicate insights
- Understand gold's role in the global financial system

## 🎯 Key Findings

- Strong inverse correlation between gold prices and USD strength
- Gold acts as a hedge during market volatility (VIX correlation)
- Real interest rates significantly impact gold demand
- Emerging market growth (China) influences gold consumption patterns

## 📁 Repository Structure (Reorganized)

```
data/
  raw/                       # Original source datasets
    gold_longterm_drivers.xlsx
  processed/                 # Cleaned / transformed tables
    gold_dataset_final.xlsx

notebooks/
  01_data_cleaning.ipynb     # Loading & initial cleaning
  02_eda.ipynb               # Exploratory data analysis
  03_gold_vs_macro.ipynb     # Relationships gold vs macro drivers
  04_final_plots.ipynb       # Final visual assets for reporting

src/
  data_prep/
    load_data.py             # Centralized loading utilities
    clean_data.py            # Column normalization & basic cleaning
  analysis/
    time_series.py           # Quarterly resampling helpers
    correlations.py          # Correlation computation utilities
    macro_relations.py       # Lagged relationships & macro impact
  utils/
    config.py                # Path / configuration constants
    plotting.py              # Reusable plotting helpers

reports/
  figures/                   # (Generated plots exported manually)
  dashboards/
    oro_y_poder.pbix         # Power BI interactive dashboard
  final_presentation.pdf     # Summary deck

docs/
  overview.md
  methodology.md
  data_sources.md

requirements.txt
.gitignore
README.md
LICENSE
```

## ❓ Key Questions & Hypotheses

1. How strongly do real interest rates explain quarterly movements in gold prices?
2. Does gold consistently act as a hedge during spikes in market volatility (VIX)?
3. Is USD weakness (broad dollar index) a leading indicator for gold rallies?
4. Do emerging market growth metrics (e.g., China GDP) align with structural demand trends?
5. Are debt sustainability signals (US Debt/GDP) associated with flight-to-safety flows into gold?

## 🧪 Methods & Approach

- Data ingestion via FRED & World Bank APIs (scripted logic in original notebooks)
- Frequency normalization: daily/monthly series aggregated to quarterly (mean or forward fill)
- Feature engineering: YoY inflation, lag correlations, macro alignment
- Exploratory Data Analysis: distribution checks, correlation matrices, time-series overlays
- Macro relationship assessment: lagged correlation analysis & comparative trend inspection
- Visualization: Python (matplotlib/seaborn) + Power BI (interactive filtering & breakdowns)

## 🔄 How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Open notebooks in order
jupyter notebook notebooks/

# 3. (Optional) Use src/ modules inside notebooks
from src.data_prep.load_data import load_gold_longterm
```

Power BI dashboard: open `reports/dashboards/oro_y_poder.pbix` in Power BI Desktop.

## 💡 Summary of Insights (Condensed)

- Real rates remain the dominant macro driver (inverse linkage).
- Periods of elevated volatility (VIX) coincide with defensive bids for gold.
- Sustained USD softness amplifies multi-quarter gold advances.
- Structural demand (China growth) provides a supportive backdrop rather than short-term timing signal.
- Debt burden metrics align with longer-term safe-haven narratives rather than immediate price pivots.

## 🚀 Future Improvements

- Add automated API refresh pipeline (scheduled job / script).
- Introduce multivariate regression / ML feature importance ranking.
- Expand geographic demand segmentation (India, Middle East, ETF flows).
- Integrate forecasting (ARIMA / Prophet) for scenario testing.
- Containerize environment for reproducibility (Docker).

## 🛠️ Technologies Used

- **Python 3.9+**
  - pandas: Data manipulation and analysis
  - pandas-datareader: Economic data from FRED API
  - World Bank API: International economic indicators
  - matplotlib/seaborn: Data visualization
  - openpyxl: Excel file handling

- **Power BI Desktop**
  - Interactive dashboards
  - Advanced DAX calculations
  - Time series visualizations

## 📡 Data Sources (Detailed)

| Source | Purpose | Example Series / Identifier |
|--------|--------|-----------------------------|
| FRED (Federal Reserve) | Macro & market indicators | `DTWEXBGS` (USD Index), `DFII10` (US 10Y TIPS real rate), `CPIAUCSL` (CPI), `DCOILBRENTEU` (Brent Oil), `SP500` (S&P 500), `VIXCLS` (VIX), `GFDEGDQ188S` (US Debt/GDP) |
| World Bank | Global growth metrics | `NY.GDP.MKTP.KD.ZG` (China GDP growth % real) |
| World Gold Council | Gold production & reserves | Annual production volumes, official holdings |
| IMF / International Statistics | Monetary reserves context | Global FX reserves, gold reserve reports |

You can refresh the dataset by re-running `notebooks/dataset_builder.ipynb` (requires internet access). All quarterly transformations are performed in-code via resampling utilities.

### FRED Series Retrieval Quick Reference
```python
fred_series = [
  "DTWEXBGS",      # USD Broad Index
  "DFII10",        # 10Y TIPS Real Rate
  "CPIAUCSL",      # CPI (processed to YoY inflation)
  "DCOILBRENTEU",  # Brent Oil Price
  "SP500",         # S&P 500 Index
  "VIXCLS",        # Volatility Index
  "GFDEGDQ188S"    # US Debt/GDP Ratio
]
```

### World Bank Indicator
```python
wb_indicator = "NY.GDP.MKTP.KD.ZG"  # China real GDP growth (% change)
```

### Quarterly Transformation Helpers (Excerpt)
```python
def to_quarter_avg(s):
  s = pd.Series(s).dropna()
  s.index = pd.to_datetime(s.index)
  return s.resample("Q").mean()

def to_quarter_ffill(s):
  s = pd.Series(s).dropna()
  s.index = pd.to_datetime(s.index)
  return s.resample("Q").ffill()
```

## 📊 Power BI Dashboard Enhancements

The `powerbi/oro_y_poder.pbix` file contains:
- Dynamic time-series comparison between gold price and macro drivers.
- Slicers for date range, driver selection, and regional gold reserves.
- DAX measures for YoY change, rolling averages, and volatility scoring.
- Correlation visuals aligning gold movements with USD strength and real rates.

### Updating the Dashboard
1. Refresh data connections (if pointing to local processed Excel files).
2. Re-run the dataset builder notebook for latest macro data.
3. Export visuals for reports (File > Export > PDF or PowerPoint).
4. Optional: Publish to Power BI Service for cloud sharing.

### Recommended Additional Visuals (Future Work)
- Decomposition tree: Gold price contributors per quarter.
- Scatter matrix: Multi-driver comparative influence.
- Forecast visual: ARIMA or Prophet integration via R/Python script in Power BI.

## 📈 Dataset Description

**Time Period:** Q1 2014 - Q4 2024 (Quarterly data)

**Variables Analyzed:**
- Gold prices (USD/oz)
- USD Index (DXY)
- US Real Interest Rates (10Y TIPS)
- US Inflation (CPI YoY %)
- Oil Prices (Brent crude)
- S&P 500 Index
- VIX (Volatility Index)
- China GDP Growth
- US Government Debt/GDP ratio
- Global gold reserves
- Gold mining production

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.9 or higher
Power BI Desktop (for .pbix files)
```

### Installation

1. Clone the repository
```bash
git clone https://github.com/rAmIro-89/gold-market-macroeconomic-analysis.git
cd gold-market-macroeconomic-analysis
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the notebooks
```bash
jupyter notebook notebooks/
```

### Running the Analysis

1. **Data Collection:** Open `notebooks/dataset_builder.ipynb` to see how the dataset was constructed from multiple APIs
2. **Exploratory Analysis:** Open `notebooks/gold_analysis.ipynb` for in-depth analysis and visualizations
3. **Interactive Dashboard:** Open `powerbi/oro_y_poder.pbix` in Power BI Desktop

## 📊 Power BI Dashboard

The Power BI dashboard includes:
- Time series analysis of gold prices vs macroeconomic indicators
- Correlation matrices and heatmaps
- Regional analysis of gold reserves and production
- Interactive filters for custom analysis

## 🔍 Methodology

1. **Data Collection:** Automated data extraction from FRED and World Bank APIs
2. **Data Cleaning:** Handling missing values, outliers, and data alignment
3. **Feature Engineering:** Creating quarterly aggregations and derived metrics
4. **Exploratory Data Analysis:** Statistical analysis and visualization
5. **Dashboard Development:** Interactive Power BI reporting

For detailed methodology, see [docs/methodology.pdf](docs/methodology.pdf)

## 📝 Key Insights

### 1. Gold as Safe Haven
Gold prices increase during periods of market uncertainty (high VIX), confirming its role as a safe-haven asset.

### 2. Currency Impact
Strong inverse correlation (-0.65) between gold prices and USD index, demonstrating gold's role as a dollar hedge.

### 3. Real Rates Matter
Real interest rates are the strongest predictor of gold prices - when real rates decline, gold becomes more attractive.

### 4. Emerging Market Demand
China's GDP growth shows positive correlation with gold consumption, highlighting importance of emerging market demand.

## 🎓 Skills Demonstrated

- **Data Engineering:** API integration, data pipelines, ETL processes
- **Data Analysis:** Statistical analysis, correlation studies, trend analysis
- **Data Visualization:** Power BI dashboards, Python plotting libraries
- **Domain Knowledge:** Macroeconomics, financial markets, commodities
- **Tools:** Python, Jupyter, Power BI, Excel, Git

## 📫 Contact

**Ramiro Ottone Villar**
- GitHub: [@rAmIro-89](https://github.com/rAmIro-89)
- LinkedIn: [Your LinkedIn Profile]
- Email: [Your Email]

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Federal Reserve Economic Data (FRED) for economic data
- World Bank for international indicators
- World Gold Council for gold market data
- IMF for global financial statistics

---

⭐ If you find this project useful, please consider giving it a star!
