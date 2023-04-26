from typing import List

def column_name_reformating(df):
    """rename all Pandas columns to a lowercase/underscore format"""


    old_columns: List[str] = df.columns
    new_columns = []

    for column in old_columns:
        new_columns.append(column.lower().replace(" ", "_").replace("(", "").replace(")", ""))

    df.columns = new_columns
    return df
