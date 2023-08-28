import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee['salary'].drop_duplicates()
    df = df.sort_values(ascending=False)
    if N > len(df):
        return pd.DataFrame({'Nth Highest Salary': [None]})
    df = df.iloc[N - 1]
    return pd.DataFrame({'Nth Highest Salary': [df]})
