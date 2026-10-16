"""Small reusable helpers for data investigation."""
import pandas as pd


def load_csv(path, **kwargs):
    """Load a CSV and print its shape."""
    df = pd.read_csv(path, **kwargs)
    print(f"Loaded {path}: {df.shape[0]:,} rows x {df.shape[1]} columns")
    return df


def quick_look(df, n=5):
    """Print head, dtypes, missing values and summary stats."""
    print(df.head(n).to_string())
    print("
Dtypes:")
    print(df.dtypes.to_string())
    print("
Missing values:")
    print(df.isna().sum().to_string())
    print("
Summary:")
    print(df.describe(include="all").to_string())
