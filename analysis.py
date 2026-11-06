import pandas as pd
import numpy as np

def generate_business_report():
    np.random.seed(42)
    data = {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Sales': np.random.randint(10000, 50000, size=6),
        'Expenses': np.random.randint(5000, 25000, size=6)
    }
    df = pd.DataFrame(data)
    df['Profit'] = df['Sales'] - df['Expenses']
    
    print("--- Business Analytics Report ---")
    print(df)
    print("\nTotal Sales:", df['Sales'].sum())
    print("Total Profit:", df['Profit'].sum())

if __name__ == "__main__":
    generate_business_report()
