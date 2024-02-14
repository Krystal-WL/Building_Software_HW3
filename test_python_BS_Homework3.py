
import pytest
import pandas as pd
from python_BS_Homework3 import rename_column

def test_rename_column_results():
    # create a DataFrame with '_id' and 'other_columns' columns
    inputs = pd.DataFrame({'_id': [1, 2, 3], 'other_columns': [4, 5, 6]})

    # execute the rename_column() function on the DataFrame
    out = rename_column(inputs)

    # Assert that '_id' has been renamed to 'ID', and '_id' no longer exists
    assert 'ID' in out.columns and '_id' not in out.columns


def test_rename_column_errors():
    # Create a DataFrame without an '_id' column
    inputs = pd.DataFrame({'some_column': [1, 2, 3], 'other_column': [4, 5, 6]})
    
    # Expect ValueError to be raised because '_id' column is missing
    with pytest.raises(ValueError):
        rename_column(inputs)