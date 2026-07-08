import pytest
import pandas as pd
import .etl as etl

def test_transform():
    df = pd.DataFrame({'id': [101, 102, 103],'name': ['Alice', 'Bob', 'David'], 'age': [25, 30, 22], 'city': ['New York', 'Los Angeles', 'Chicago'], 'salary': [50000, 60000, 80000]})
    df = etl.transform_data(df)
    assert df['net_salary'].tolist() == [45000.0, 54000.0, 72000.0]
