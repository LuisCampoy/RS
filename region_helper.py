# Recovery Score Calculations: Calculation helper
# Script created  3/25/2024
# Last revision 5/16/2024

import pandas as pd


# calculate maximum absolute value within the ROI in X, Y and Z axis
def get_region(df, regions_of_interest, window_size, step_size):

    for k in range(len(regions_of_interest)):
        print(
            "ROI ",
            k + 1,
            ": (",
            df["TimeStamp"][regions_of_interest[k][0] * step_size],
            ",",
            df["TimeStamp"][regions_of_interest[k][0] * step_size + window_size],
            ")",
        )


def get_max_abs_value(df, regions_of_interest, window_size, step_size) -> list[float]:
    """Create a new pd.DataFrafe with the 3 columns (AccX, AccY, AccZ) within each region of interest
        Calculate abs value of each colum and then the max value of each column
        Do this for for each failed attemp (all except for the last one)
        Do the same for the last attempt but using only AccY and AccX

    Args:
        df:
        regions_of_interest:
        window_size:
        step_size

    Returns:
        list[float]

    """

    raise NotImplementedError("get_max_abs_value is missing code")

    # Assuming 'df' is your DataFrame and x, y are the row indices
    # Replace 1 and 4 with the column indices if needed (Python uses 0-based indexing)

    for i in range(len(regions_of_interest)):

        selected_data = df.loc[
            [regions_of_interest[i][0] * step_size] : [
                regions_of_interest[i][0] * step_size + window_size
            ],
            1:4,
        ]

        print(f"selected_data are... {selected_data}")

        max_abs_value = selected_data.abs().max().max()

    return max_abs_value
