import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df1 = pd.merge(orders, company, on='com_id', how='inner')
    df2 = df1[df1['name'] == 'RED']['sales_id'].unique()
    df = sales_person[~sales_person['sales_id'].isin(df2)][['name']]
    return df
