import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    
    df = patients[patients['conditions'].str.contains(r'\bDIAB1')]
    df = df[['patient_id', 'patient_name', 'conditions']]
    return df
