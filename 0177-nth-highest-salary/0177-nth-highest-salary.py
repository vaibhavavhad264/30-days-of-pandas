# 21/08/2026
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    column_name = f'getNthHighestSalary({N})'
    
    if N <= 0 or len(salaries) < N:
        return pd.DataFrame({column_name: [None]})
    
    return pd.DataFrame({ column_name : [salaries.iloc[N - 1] ]})