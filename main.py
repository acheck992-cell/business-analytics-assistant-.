import pandas as pd
import numpy as np

def generate_analytics_report():
    np.random.seed(42)
    dates = pd.date_range(start='2026-01-01', periods=30, freq='D')
    revenue = np.random.uniform(1000, 5000, size=30).round(2)
    customers = np.random.randint(50, 200, size=30)
    
    df = pd.DataFrame({
        'Date': dates,
        'Revenue': revenue,
        'Customers': customers
    })
    
    print("--- AI Business Analytics Summary ---")
    print(df.head())
    print("\nTotal Revenue:", df['Revenue'].sum())
    print("Average Customers per Day:", df['Customers'].mean())

if __name__ == "__main__":
    generate_analytics_report()
