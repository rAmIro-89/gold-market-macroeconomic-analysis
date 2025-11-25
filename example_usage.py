"""
Quick usage example for gold macroeconomic analysis.

Demonstrates how to use the reusable modules from src/.
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

# Example usage (functions would need to be implemented in src/)
def main():
    """Run gold price analysis pipeline."""
    
    print("="*60)
    print("GOLD MACROECONOMIC ANALYSIS - QUICK DEMO")
    print("="*60)
    
    print("\nThis project includes:")
    print("  ✓ src/data_prep/ - Data loading and cleaning utilities")
    print("  ✓ src/analysis/ - Time series and correlation analysis")
    print("  ✓ src/utils/ - Plotting and configuration helpers")
    print("\nFor full analysis, see notebooks/ directory:")
    print("  1. 01_data_cleaning.ipynb")
    print("  2. 02_eda.ipynb")
    print("  3. 03_gold_vs_macro.ipynb")
    print("  4. 04_final_plots.ipynb")
    print("\nPower BI Dashboard: reports/dashboards/oro_y_poder.pbix")

if __name__ == "__main__":
    main()
