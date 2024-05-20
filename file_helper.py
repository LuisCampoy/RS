# Recovery Score Calculations: file_helper Script
# Script created  3/25/2024
# Last revision 5/19/2024

import pandas as pd


def read_csv_file(file_path) -> pd.DataFrame:
    """Read the first four columns (TimeStamp, AccX, AccY, AccZ) from the csv file
        using the read_csv function.
        skips the first row (Sep = ,)
        Uses the second row as header
        only reads the first 4 rows to speed file reading time

    Args:
        file_path: cvs file's name

    Returns:
        Pandas DataFrame
    """
    try:
        print("reading csv file...")

        df: pd.DataFrame = pd.read_csv(
            file_path,
            skiprows=1,
            sep=",",
            header=0,
            usecols= [1, 2, 3, 4],
            encoding="utf-8",
            low_memory=False,
        )

        df = df.drop(index=0)

        print(df.head())
        print(df.tail())
        print("file read")

        return df

    except Exception as e:

        print("An error occurred:", str(e))

    return None