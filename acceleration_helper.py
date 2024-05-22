# Recovery Score Calculations: Acceleration helper
# Script created  3/25/2024
# Last revision 5/22/2024

import pandas as pd

def get_amax_sa(df, regions_of_interest, window_size, step_size):
    """Create a new pd.DataFrafe with the 2 columns (AccX, AccY) within the last region of interest (successful attempt)
        Creat start index and end index from...???
        Calculate abs value of each colum and then return the max value from each column

    Args:
        df:
        regions_of_interest:
        window_size:
        step_size:

    Returns:
        list[float]

    """

    #raise NotImplementedError("Sorry, get_amax_sa() is not implemented yet...")
    
    j=len(regions_of_interest) +1
    
    start_index = regions_of_interest[j][0] * step_size
    end_index = start_index + window_size

        # Select rows using iloc and columns using column names
    selected_data = df.iloc[start_index:end_index][['AccX', 'AccY']]
        
        # Display the selected data
    print(f"Region {j}:")
    print(selected_data)
    print()

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