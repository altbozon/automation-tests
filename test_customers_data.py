import pandas as pd

# Load the CSV
df = pd.read_csv("customers.csv")

# CLEAN the column names
df.columns = df.columns.str.strip().str.replace('"', '').str.replace(' ', '')

# Test 1: No missing values
def test_no_missing_values():
    assert not df.isnull().values.any(), "There are missing values!"

# Test 2: Height and Weight must be positive
def test_positive_height_weight():
    assert (df["Height(Inches)"].apply(lambda x: float(x) > 0)).all(), "Some heights are not positive!"
    assert (df["Weight(Pounds)"].apply(lambda x: float(x) > 0)).all(), "Some weights are not positive!"
