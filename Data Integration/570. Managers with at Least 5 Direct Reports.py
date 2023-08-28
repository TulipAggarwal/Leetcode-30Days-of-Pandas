import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby('managerId').size().reset_index(name='directReports')
    df = df[df['directReports'] >= 5]
    df = df.merge(employee[['id', 'name']], left_on='managerId', right_on='id', how='inner')
    df = df[['name']]
    return df
