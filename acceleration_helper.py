# Recovery Score Calculations: Acceleration helper
# Script created  3/25/2024
# Last revision 5/22/2024

import pandas as pd

def get_amax_sa():
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

    raise NotImplementedError("Sorry, get_amax_sa() is not implemented yet...")
  
    
def get_amax_ua():
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

    selected_data_list = []

    # Loop through each region of interest
    for j in range(len(regions_of_interest)):
        start_index = regions_of_interest[j][0] * step_size
        end_index = start_index + window_size

        # Select rows using iloc and columns using column names
        selected_data = df.iloc[start_index:end_index][["TimeStamp", "AccX", "AccY"]]
        selected_data_list.append(selected_data)

    # Concatenate all selected data into a single DataFrame
    all_selected_data = pd.concat(selected_data_list).reset_index(drop=True)

    # Display the resulting DataFrame
    print(all_selected_data)
