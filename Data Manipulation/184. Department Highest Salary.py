import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on = 'departmentId', right_on = 'id')
    df = df.rename(columns = {'name_x': 'Employee', 'name_y': 'Department', 'salary': 'Salary'})[['Department', 'Employee', 'Salary']]
    return df[df['Salary'] == df.groupby('Department')['Salary'].transform(max)]
