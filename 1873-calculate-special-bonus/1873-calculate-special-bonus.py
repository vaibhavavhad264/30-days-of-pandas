# 16/08/2026
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda x: x['salary'] if x['employee_id'] % 2 == 1 and not x['name'].startswith('M')
        else 0,
        axis=1)
    df = employees[['employee_id', 'bonus']]
    return df.sort_values(by = 'employee_id')