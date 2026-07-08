import pytest
import pandas as pd
import etl as e

def test_load():
    df = pd.DataFrame({'id': [101, 102, 103],'name': ['Alice', 'Bob', 'David'], 'age': [25, 30, 22], 'city': ['New York', 'Los Angeles', 'Chicago'], 'salary': [50000, 60000, 80000]})
    file_path = e.load_data(df, 'data/test_data.csv')
    file = pd.read_csv('data/test_data.csv')
    assert not file.empty