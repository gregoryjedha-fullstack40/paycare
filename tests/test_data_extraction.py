import pytest
import .etl as etl

def test_extract():
    filepath = 'data/input_data.csv'
    df = etl.extract_data(filepath)
    assert not df.empty
