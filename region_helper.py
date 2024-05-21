# Recovery Score Calculations: Calculation helper
# Script created  3/25/2024
# Last revision 5/16/2024

import pandas as pd


# calculate maximum absolute value within the ROI in X, Y and Z axis
def get_region(df, regions_of_interest, window_size, step_size):

    for j in range(len(regions_of_interest)):
        print(
            "ROI ",
            j + 1,
            ": (",
            df["TimeStamp"][regions_of_interest[j][0] * step_size],
            ",",
            df["TimeStamp"][regions_of_interest[j][0] * step_size + window_size],
            ")",
        )


def get_amax_sa(df, regions_of_interest, window_size, step_size) -> list[float]:
    """Create a new pd.DataFrafe with the 2 columns (AccX, AccY) within the last region of interest (successful attempt)
        Calculate abs value of each colum and then return the max value from each column

    Args:
        df:
        regions_of_interest:
        window_size:
        step_size:

    Returns:
        list[float]

    """

    raise NotImplementedError("Sorry, get_amax_sa() is not implemented yet...")

    j = len(regions_of_interest)
    window = []
    for region in regions_of_interest:
        start_index = region[0] * step_size
        end_index = start_index + window_size

        AccX_val = df["AccX"][start_index]
        AccY_val = df["AccY"][end_index]

        window.append((AccX_val, AccY_val))

    selected_data = pd.DataFrame(window, columns=["AccX", "AccY"])

    # selected_data = df.loc[[regions_of_interest[j][0] * step_size] : [regions_of_interest[j][0] * step_size + window_size]]
    # selected_data = df.iloc[regions_of_interest[0][0] : regions_of_interest[0][0] + window_size,"AccX":"AccY"]

    print(selected_data)
    print("Selected_Data printed...")

    # amax_sa = selected_data.abs().max().max()

    # return amax_sa


def get_amax_ua(df, regions_of_interest, window_size, step_size) -> list[float]:
    """Create a new pd.DataFrafe with the 3 columns (AccX, AccY, AccZ) within each region of interest
        Calculate abs value of each colum and then the max value of each column
        Do this for for each failed attemp (all except for the last one)

    Args:
        df:
        regions_of_interest:
        window_size:
        step_size

    Returns:
        list[float]

    """

    raise NotImplementedError("Sorry, get_amax_ua() is not implemented yet...")

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

        max_sa = selected_data.abs().max().max()

    return max_
