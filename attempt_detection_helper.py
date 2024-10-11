# Recovery Score Calculations: Identification of Regions of Interest helper
# Script created  3/25/2024
# Last revision 10/9/2024

import numpy as np

def calculate_window_sd(df, window_size, step_size)-> list:
    ''' Creates a window to scan the data. The window size is 'window_size' data points and the window is advancing every 'step_size' datapoints.
        Function calculates the standard deviation (SD) over a specified window size with a specified step size

    Args:
        filtered_df: extracted column (Shimmer_4DA1_Accel_LN_Z_CAL)
                     with initial filtered values >= target value
        window_size: window size
        step_size: number of data points by which the window advances

    Returns:
        list of float values
    '''
    
    print('calculating window_sd...')

    n: int = len(df)
    sd_list: list = []
    for i in range(0, n - window_size + 1, step_size):
        window = df[i : i + window_size]
        sd = np.std(window)
        sd_list.append(sd)
    
    return sd_list

def detect_regions_of_interest_Z(AccZ_sd, threshold) -> list:
    ''' Identifies Regions of Interest in the data based on a threshold criterion 
        applied to the standard deviation values (AccZ_sd)
        It filters out regions where the standard deviation is greater than or equal to twice 
        the threshold value (threshold * 2). These regions are stored in the filtered list along with their indexes.

    Args:
        AccZ_sd: list with the all the regions that have a standad deviation greater or equal to twice the threshold
        
    Returns:
        list with the regions of interest
    '''

    filtered = list()
    
    for i in range(len(AccZ_sd)):
        if AccZ_sd[i] > threshold:
            filtered.append((i, AccZ_sd[i]))

    regions_of_interest = list()
    big = 0
    index = 0
    for j in range(len(filtered) - 1):
        if filtered[j][0] + 1 == filtered[j + 1][0]:
            if filtered[j][1] > big:
                big = filtered[j][1]
                index = filtered[j][0]
            elif filtered[j + 1][1] > big:
                big = filtered[j + 1][1]
                index = filtered[j + 1][0]
        elif big > 0:
            regions_of_interest.append((index, big))
            big = 0
            index = 0
        
    regions_of_interest.append((index, big))
    
    return regions_of_interest

def get_attempts(regions_of_interest: list) ->int:
    ''' Counts the number of identified regions of interest. Since the last region will always be
        the successful attempt, it substracts 1 to the final count

    Args:
        regions_of_interest: list with the all the regions that have a standad deviation > set threshold

    Returns:
        int with Number of failed Attempts
    '''

    attempts: int = len(regions_of_interest) - 1

    return attempts
