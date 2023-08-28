import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='cooperation_count')
    df = df[df['cooperation_count'] >= 3]
    return df[['actor_id', 'director_id']]
