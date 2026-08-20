# 20/08/2026
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders['customer_number'].value_counts()
    return pd.DataFrame({
        'customer_number' : [df.idxmax()]
    })