import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    df = scores.drop('id',axis=1).sort_values(by='score', ascending=False)
    return df
