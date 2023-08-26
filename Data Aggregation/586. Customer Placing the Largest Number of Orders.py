import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    
    df = orders.groupby('customer_number')['order_number'].count().reset_index()
    df = df[df['order_number'] == df['order_number'].max()][['customer_number']]
    return df
