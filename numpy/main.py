import pandas as pd
from typing import List
from prettytable import PrettyTable


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    data = {
        'student_id': ['101', '102', '103'],
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [20, 21, 22]}
    students = pd.DataFrame(data)
    return students.loc[students['student_id'] == '101', ['name', 'age']]





if __name__ == '__main__':
    print(selectData(pd.DataFrame([[101,15],[2,11],[3,11],[4,20]], columns=['student_id', 'asdf'])))