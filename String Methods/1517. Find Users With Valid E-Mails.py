import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r"^[A-Za-z][-._A-Za-z0-9]*@leetcode\.com$"
    filterr = users['mail'].str.match(pattern)
    df = users[filterr]
    return df
