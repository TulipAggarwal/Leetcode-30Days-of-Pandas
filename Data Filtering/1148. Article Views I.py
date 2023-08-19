import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[(views['author_id'] == views['viewer_id'])]
    df = df['author_id'].unique()
    df = sorted(df)
    df = pd.DataFrame({'id': df})
 
    return df
