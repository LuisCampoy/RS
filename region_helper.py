# Recovery Score Calculations: Calculation helper
# Script created  3/25/2024
# Last revision 5/23/2024

import pandas as pd

# calculate maximum absolute value within the ROI in X, Y and Z axis
def get_regions(df, regions_of_interest, window_size, step_size)-> tuple:
    '''Provides len(regions_of_interest) DataFrames with a selected regions of interest
    
    Args:
        df: pd.DataFrame provided
        regions_of_interest: list of tuples with the start and the end of each of the regions that have a standad deviation > our threshold
        window_size (int): size of each window
        step_size (int):step_size for the window
        
    Returns:
        Tuple: Containing a list of DataFrames, each DataFrame contains a specific region of interest, 
               and three lists with maximum absolute values of AccX, AccY, and AccZ for each region.
    '''
    # Store data from each reion of interest
    selected_data_list: list = [] 
    # Store data from the maximum acceleration values from each axis and each region
    amax_x_region: list = []
    amax_y_region: list = []
    amax_z_region: list = []
    
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
           
        '''# Print timestamps for debugging
        start_time = df['TimeStamp'].iloc[start_index]
        end_time = df['TimeStamp'].iloc[end_index - 1]  # Subtract 1 to get the correct end timestamp
        print(f'ROI {i + 1}: ({start_time}, {end_time})')
        print(selected_data)'''
        
        # Append and calculate the maximum absolute value of each axis in each region
        amax_x_region.append(selected_data['AccX'].abs().max())
        amax_y_region.append(selected_data['AccY'].abs().max())
        amax_z_region.append(selected_data['AccZ'].abs().max())
         
    return selected_data_list, amax_x_region, amax_y_region, amax_z_region

        

    
   
    
    

        
              
      