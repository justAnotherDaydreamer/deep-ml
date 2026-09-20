import pandas as pd

def solution(df):
    kept_rows = df[df['status'] == "completed"]

    region_only = kept_rows.groupby(by='region', as_index=False)['amount'].sum()

    sorted_region_only = region_only.sort_values(by='amount', ascending=False)

    output = sorted_region_only.iloc[0:10, :]
    return output