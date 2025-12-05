# Gold Market & Macroeconomic Analysis

![Project Status](https://img.shields.io/badge/status-completed-success)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Jupyter](https://img.shields.io/badge/jupyter-notebooks-orange)
![Pandas](https://img.shields.io/badge/pandas-data%20analysis-150458)
![Plotly](https://img.shields.io/badge/plotly-visualization-3F4F75)
![License](https://img.shields.io/badge/license-MIT-green)

> **A comprehensive macro-financial analysis exploring the relationship between gold prices and global economic indicators through advanced time-series modeling and statistical analysis.**

## Problem Statement

Gold serves as both a commodity and a financial asset, acting as a hedge against inflation, currency devaluation, and economic uncertainty. However, understanding the complex interplay between gold prices and macroeconomic variables requires sophisticated analytical approaches:

- **Market volatility** makes traditional correlation analysis insufficient
- **Multiple driving factors** (inflation, interest rates, currency strength, geopolitical risk) interact simultaneously
- **Physical market dynamics** (supply, demand, central bank reserves) add complexity
- **Long-term trends vs. short-term fluctuations** require different analytical lenses

This project provides a data-driven framework to quantify these relationships, helping investors, analysts, and researchers understand gold market behavior through the lens of macroeconomic fundamentals.

---

## Key Findings

### 1. **Inverse USD-Gold Relationship**
- **Strong negative correlation** between USD Index and gold prices (-0.72 average)
- Dollar weakness consistently drives gold appreciation
- Rolling correlation windows reveal periods of divergence during market stress

### 2. **Gold as Inflation Hedge**
- Positive correlation with CPI increases during high-inflation periods
- Real interest rates (nominal rate - inflation) show **strongest predictive power**
- When real rates turn negative, gold outperforms significantly

### 3. **Gold/Oil Ratio Insights**
- Historical mean: ~15-20 barrels of oil per ounce of gold
- Ratio spikes above 30 indicate gold overvaluation or oil undervaluation
- Provides actionable reversion-to-mean trading signals

### 4. **Central Bank Accumulation**
- Central banks increased gold reserves by 400+ tonnes annually (2010-2023)
- Emerging markets (China, Russia, India) driving demand
- Supply constraints from mining production create structural support

---

## Features & Analysis

### 1. Technical Analysis & Risk Metrics
- **Gold vs USD Index**: Inverse relationship visualization with rolling correlations
- **Gold/Oil Ratio**: Moving averages and historical mean reversion analysis
- **Volatility Analysis**: Rolling standard deviation and trend shift detection
- **Risk Indicators**: Drawdown analysis and support/resistance levels

![Technical Analysis](img/01-technical-analysis-gold-risks.png)
*Figure 1: Technical indicators showing gold price dynamics and correlation with USD Index*

---

### 2. Macroeconomic Drivers
- **Inflation Impact**: CPI correlation with gold price movements
- **Real Interest Rates**: Fisher equation application (nominal rate - inflation)
- **Currency Strength**: DXY (Dollar Index) multivariate analysis
- **Long-Term Trends**: Decade-scale relationships and regime shifts

![Macro Indicators](img/02-macro-indicators-gold-price.png)
*Figure 2: Macroeconomic variables and their relationship with gold prices over time*

---

### 3. Physical Gold Market Analysis
- **Supply & Demand Dynamics**: Mining production, recycling, jewelry, investment
- **Supply-Demand Balance**: Quarterly net positioning and market imbalances
- **Central Bank Reserves**: Official sector purchases and strategic accumulation
- **Market Fundamentals**: Physical market impact on price formation

![Physical Market](img/03-physical-gold-market.png)
*Figure 3: Global gold supply, demand, and central bank reserve trends*

---

## Methodology

### Data Collection & Processing
- **Data Sources**: FRED (Federal Reserve Economic Data), World Bank, World Gold Council, IMF
- **Time Period**: 1990-2023 (33 years of historical data)
- **Frequency**: Monthly and quarterly data aligned to common timeframes
- **Data Cleaning**: Missing value imputation, outlier detection, normalization

### Statistical Techniques
- **Time-Series Analysis**: Trend decomposition, seasonality detection, stationarity tests
- **Correlation Analysis**: Pearson correlation, rolling window correlations, lead-lag relationships
- **Feature Engineering**: Log returns, percentage changes, moving averages (20/50/200-day)
- **Ratio Analysis**: Gold/Oil, Gold/Silver, Real vs. Nominal price adjustments

### Visualization & Reporting
- **Python Libraries**: Matplotlib, Seaborn, Plotly for interactive charts
- **Jupyter Notebooks**: Reproducible analysis pipeline with narrative documentation
- **Multi-Panel Dashboards**: Comprehensive views combining technical, macro, and physical market data

---

## Project Structure

```
gold-market-macroeconomic-analysis/
│
├── notebooks/                      # Analysis pipeline
│   ├── 01_data_cleaning.ipynb     # Data ingestion and preprocessing
│   ├── 02_eda.ipynb               # Exploratory data analysis
│   ├── 03_gold_vs_macro.ipynb     # Correlation and regression analysis
│   └── 04_final_plots.ipynb       # Publication-quality visualizations
│
├── data/                           # Datasets
│   ├── raw/                       # Original data from sources
│   └── processed/                 # Cleaned and transformed data
│
├── img/                            # Analysis outputs
│   ├── 01-technical-analysis-gold-risks.png
│   ├── 02-macro-indicators-gold-price.png
│   └── 03-physical-gold-market.png
│
├── src/                            # Utility modules (optional)
├── docs/                           # Additional documentation
├── requirements.txt                # Python dependencies
├── example_usage.py               # Quick demo script
└── README.md                       # This file
```

---

## Getting Started

### Prerequisites
- Python 3.9 or higher
- Jupyter Notebook or JupyterLab
- Git (for cloning the repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rAmIro-89/gold-market-macroeconomic-analysis.git
   cd gold-market-macroeconomic-analysis
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Analysis

**Option 1: Execute All Notebooks Sequentially**
```bash
jupyter notebook notebooks/01_data_cleaning.ipynb
```
Then run notebooks in order: `01 → 02 → 03 → 04`

**Option 2: Quick Demo Script**
```bash
python example_usage.py
```
Generates sample outputs and key statistics without opening notebooks.

**Option 3: Interactive Exploration**
```bash
jupyter lab
```
Open any notebook and explore analysis interactively.

---

## Technologies & Dependencies

| Category | Tools |
|----------|-------|
| **Data Processing** | Pandas 1.5+, NumPy 1.24+ |
| **Data Sources** | pandas-datareader (FRED API integration) |
| **Visualization** | Matplotlib 3.5+, Seaborn 0.12+, Plotly 5.0+ |
| **Statistical Analysis** | SciPy 1.10+, Statsmodels 0.14+ |
| **Notebook Environment** | Jupyter, IPython |
| **Configuration** | python-dotenv (for API keys) |

See `requirements.txt` for complete dependency list.

---

## Key Insights for Investors

### When to Consider Gold Exposure:
✅ **Real interest rates turning negative** (nominal rate < inflation)  
✅ **USD Index weakening** (DXY trending below 95)  
✅ **Central bank accumulation accelerating** (quarterly purchases > 100 tonnes)  
✅ **Gold/Oil ratio > 25** (potential mean reversion opportunity)  

### When to Be Cautious:
⚠️ **Rising real interest rates** (Fed tightening with low inflation)  
⚠️ **Strong USD momentum** (DXY above 105)  
⚠️ **Supply-demand balance shifting to surplus**  
⚠️ **Gold/Oil ratio < 12** (gold potentially undervalued but risky)

---

## Skills Demonstrated

- **Financial Data Analysis**: Multi-source data integration, time-series preprocessing
- **Macroeconomic Reasoning**: Understanding complex relationships between economic variables
- **Statistical Modeling**: Correlation analysis, regression, rolling window techniques
- **Python Data Science Stack**: Pandas, NumPy, Matplotlib, Seaborn, Plotly, Statsmodels
- **Time-Series Analysis**: Trend decomposition, seasonality, stationarity testing
- **Data Visualization**: Publication-quality charts, multi-panel dashboards
- **Research Methodology**: Hypothesis formulation, empirical testing, interpretation
- **Storytelling with Data**: Translating complex analysis into actionable insights

---

## Future Enhancements

- [ ] Machine learning models for gold price prediction (LSTM, Random Forest)
- [ ] Real-time data pipeline with automated updates
- [ ] Interactive Power BI or Tableau dashboard
- [ ] Geopolitical risk index integration (VIX, EPU Index)
- [ ] Sentiment analysis from financial news and social media
- [ ] Portfolio optimization including gold allocation strategies

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

**Ramiro Ottone Villar**  
[![GitHub](https://img.shields.io/badge/GitHub-rAmIro--89-181717?style=flat&logo=github)](https://github.com/rAmIro-89)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/your-profile)

---

## Acknowledgments

- **Federal Reserve Economic Data (FRED)** - US macroeconomic indicators
- **World Bank** - International economic data
- **World Gold Council (WGC)** - Gold market supply/demand statistics
- **International Monetary Fund (IMF)** - Global financial data

---

⭐ **If you find this analysis valuable, please consider starring the repository!**
