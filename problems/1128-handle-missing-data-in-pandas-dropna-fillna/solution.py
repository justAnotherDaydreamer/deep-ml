import pandas as pd

def solution(df):
    # Drop columns
    cols_to_keep = [col for col in df.columns if df[col].isnull().mean() <= 0.5]
    df = df[cols_to_keep]

    # Drop rows
    # Not efficient but this is me studying ok.
    rows_to_keep = [i_row for i_row in range(df.shape[0]) if df.iloc[i_row, :].isnull().mean() <= 0.5]
    df = df.iloc[rows_to_keep, :]

    # Fill NaN
    num_cols = df.select_dtypes(include='number').columns

    for col in df.columns:
        if col in num_cols:
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode().iloc[0])

    return df