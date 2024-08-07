# Recovery Score Calculations: Calculation helper
# Script created  3/25/2024
# Last revision 7/12/2024

import pandas as pd

# calculate maximum absolute value within the ROI in X, Y and Z axis
def get_regions(filtered_df, regions_of_interest, window_size, step_size)-> tuple:
    '''Provide len(regions_of_interest) DataFrames with a selected regions of interest
    
    Args:
        df: pd.DataFrame provided
        regions_of_interest: list of tuples with the start and the end of each of the regions that have a standad deviation > our threshold
        window_size (int): size of each window
        step_size (int):step_size for the window
        
    Returns:
        Tuple: Containing a list of DataFrames, each DataFrame contains a specific region of interest, 
               and three lists with maximum absolute values of AccX, AccY, and AccZ for each region.
               Selected_Data_list is a list with a dataframe with AccX, AccY and AccZ per event
    '''
    # Store data from each reion of interest
    selected_data_list: list = [] 
    
    # Loop through each region of interest (ROI)
    for i, roi in enumerate(regions_of_interest):
        start_index = roi[0] * step_size
        end_index = start_index + window_size
        
        # Ensure the end index does not exceed the dataframe length
        if end_index > len(filtered_df):
            end_index = len(filtered_df)
            
        # Select rows using iloc and columns using column names
        selected_data = filtered_df.iloc[start_index:end_index][['AccX', 'AccY', 'AccZ']]
    
        selected_data_list.append(selected_data)
           
    return selected_data, selected_data_list

