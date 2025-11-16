import pandas as pd

def test_data_integrity():
    data = pd.read_csv("data/v2/data_augmented.csv")
    # Example sanity checks
    assert not data.isnull().values.any(), "Dataset has missing values"
    assert all(col in data.columns for col in 
               ['sepal_length','sepal_width','petal_length','petal_width','species']), \
           "Required columns missing"
    assert data['species'].nunique() == 3, "Species count mismatch"
