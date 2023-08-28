import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    df = employee['salary'].drop_duplicates()
    df = df.sort_values(ascending=False)
    if 2 > len(df):
        return pd.DataFrame({'SecondHighestSalary': [None]})
    df = df.iloc[1]
    return pd.DataFrame({'SecondHighestSalary': [df]})
