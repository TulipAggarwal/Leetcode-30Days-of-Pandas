import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df = activities.groupby('sell_date')['product'].agg(['nunique', lambda x: ','.join(sorted(set(x)))]).reset_index()
    df.columns = ['sell_date', 'num_sold', 'products']
    df['products'] = df['products'].str.replace(r'(^|,)Mask(,|$)', r'\1Mask\2')
    df = df.sort_values(by='sell_date')
    return df
