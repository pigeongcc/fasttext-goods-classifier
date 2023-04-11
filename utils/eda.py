from pprint import pprint

import pandas as pd


def get_missing_values_percentage(df: pd.DataFrame) -> pd.Series:
    return df.isna().sum().divide(len(df)).multiply(100)


def get_unique_values_percentage(df: pd.DataFrame) -> pd.Series:
    return df.nunique().divide(len(df)).multiply(100)


def eda(df: pd.DataFrame, prints: bool = True, returns: bool = False):
    missing_values_percentage = get_missing_values_percentage(df)
    unique_values_percentage = get_unique_values_percentage(df)

    if prints:
        print("Missing values percentage:")
        pprint(missing_values_percentage)
        print()

        print("Unique values percentage:")
        pprint(unique_values_percentage)
        print()
    if returns:
        return missing_values_percentage, unique_values_percentage
