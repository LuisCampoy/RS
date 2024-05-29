import pandas as pd

def get_regions(df, regions_of_interest, window_size, step_size):
    """Provides len(regions_of_interest) DataFrames with selected regions of interest and calculates maximum absolute values for AccX, AccY, and AccZ.

    Args:
        df (pd.DataFrame): The input dataframe.
        regions_of_interest (list): List of tuples with the start and end of each region that has a standard deviation > threshold.
        window_size (int): The size of each window.
        step_size (int): The step size for the window.

    Returns:
        tuple: A tuple containing a list of DataFrames, each DataFrame contains a specific region of interest, 
               and three lists with maximum absolute values of AccX, AccY, and AccZ for each region.
    """

    # Store data from each region of interest
    selected_data_list = []
    # Store maximum absolute acceleration values from each axis for each region
    amax_x_region = []
    amax_y_region = []
    amax_z_region = []
    
    # Loop through each region of interest (ROI)
    for i, roi in enumerate(regions_of_interest):
        start_index = roi[0] * step_size
        end_index = start_index + window_size
        
        # Ensure the end index does not exceed the dataframe length
        if end_index > len(df):
            end_index = len(df)
        
        # Select rows using iloc and columns using column names
        selected_data = df.iloc[start_index:end_index][['AccX', 'AccY', 'AccZ']]
        selected_data_list.append(selected_data)
        
        # Calculate the maximum absolute values for each axis in this region
        amax_x_region.append(selected_data['AccX'].abs().max())
        amax_y_region.append(selected_data['AccY'].abs().max())
        amax_z_region.append(selected_data['AccZ'].abs().max())
    
    return selected_data_list, amax_x_region, amax_y_region, amax_z_region

# Example usage:
# df is the DataFrame containing the data
# regions_of_interest = [(start1, end1), (start2, end2), ...]
# window_size = 100  # for example
# step_size = 10     # for example
# result = get_regions(df, regions_of_interest, window_size, step_size)
# selected_data_list, amax_x_region, amax_y_region, amax_z_region = result

def get_max_abs_per_axis(df: pd.DataFrame, regions_of_interest: list, window_size: int, step_size: int) -> list:
    '''Calculate the maximum absolute values per axis (AccX, AccY, AccZ) for each region of interest.
    
    Args:
        df (pd.DataFrame): Input DataFrame containing the data.
        regions_of_interest (list): List of tuples with the start and the end of each of the regions that have a standard deviation > threshold.
        window_size (int): Size of each window.
        step_size (int): Step size for the window.
        
    Returns:
        list: A list of tuples, each containing the maximum absolute values for AccX, AccY, and AccZ for a specific region of interest.
    '''
    max_abs_values = []

    # Loop through each region of interest (ROI)
    for roi in regions_of_interest:
        start_index = roi[0] * step_size
        end_index = start_index + window_size
        
        # Ensure the end index does not exceed the DataFrame length
        if end_index > len(df):
            end_index = len(df)
        
        # Select rows using iloc and columns using column names
        selected_data = df.iloc[start_index:end_index][['AccX', 'AccY', 'AccZ']]
        
        # Calculate the maximum absolute values for each axis
        max_abs_x = selected_data['AccX'].abs().max()
        max_abs_y = selected_data['AccY'].abs().max()
        max_abs_z = selected_data['AccZ'].abs().max()
        
        # Append the results as a tuple
        max_abs_values.append((max_abs_x, max_abs_y, max_abs_z))
    
    return max_abs_values