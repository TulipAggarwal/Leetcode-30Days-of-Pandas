import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    df = store[store.amount > 500]
    df = df['customer_id'].nunique()
    df = pd.DataFrame({'rich_count':[df]})
    return df
