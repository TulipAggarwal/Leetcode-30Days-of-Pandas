import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df1 = examinations.groupby(['student_id', 'subject_name']).agg(attended_exams=('subject_name', 'count')).reset_index() 
    df2 = students.merge(subjects, how='cross')
    df = df1.merge(df2, on=['student_id', 'subject_name'],how='right')
    df = df.fillna(0)
    df = df.sort_values(['student_id', 'subject_name'])
    return df[['student_id', 'student_name', 'subject_name', 'attended_exams']]
