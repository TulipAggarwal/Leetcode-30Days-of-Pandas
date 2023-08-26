import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class')['student'].count().reset_index()
    df = df[df['student'] >= 5][["class"]]
    return df
