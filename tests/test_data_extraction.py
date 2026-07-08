import pytest
import etl as e

def test_extract():
    filepath = 'data/input_data.csv'
    df = e.extract_data(filepath)
    assert not df.empty
