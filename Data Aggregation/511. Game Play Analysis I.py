import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values(by=['player_id', 'event_date'])
    df = activity.groupby('player_id')['event_date'].min().reset_index()
    df.rename(columns={'event_date': 'first_login'}, inplace=True)
    
    return df
