# Gold and Power: Macroeconomic Analysis

![Project Status](https://img.shields.io/badge/status-completed-success)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
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

## 📁 Project Structure

```
├── data/
│   ├── raw/                    # Original datasets
│   │   └── gold_longterm_drivers.xlsx
│   └── processed/              # Cleaned and transformed data
│       └── gold_dataset_final.xlsx
├── notebooks/
│   ├── dataset_builder.ipynb  # Data collection and preprocessing
│   └── gold_analysis.ipynb    # Exploratory analysis and insights
├── powerbi/
│   └── oro_y_poder.pbix       # Interactive dashboard
├── reports/
│   └── final_presentation.pdf # Project findings presentation
├── docs/
│   └── methodology.pdf        # Data collection methodology
├── src/                       # Python utility scripts
├── requirements.txt
├── .gitignore
└── README.md
```

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

- **Data Sources**
  - Federal Reserve Economic Data (FRED)
  - World Bank Open Data
  - World Gold Council
  - International Monetary Fund (IMF)

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
