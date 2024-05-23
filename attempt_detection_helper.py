# Recovery Score Calculations: Identification of Regions of Interest helper
# Script created  3/25/2024
# Last revision 5/23/2024

import pandas as pd
import numpy as np

def calculate_window_sd(data, window_size: int, step_size: int)-> list[float]:
    """ Create a window to scan the data. The window size is 'window_size' data points and the window is advancing every 'step_size' datapoints
        function calculates the standard deviation over a specified window size with a specified step size

    Args:
        data: extracted column (Shimmer_4DA1_Accel_LN_Z_CAL)
        window_size: window size
        step_size: number of data points by which the window advances

    Returns:
        list of float values
    
    """
    print('calculating window_sd...')

    n = len(data)
    sd_list = []
    for i in range(0, n - window_size + 1, step_size):
        window = data[i : i + window_size]
        sd = np.std(window)
        sd_list.append(sd)
    
    return sd_list

def detect_regions_of_interest_Z(AccZ_sd) -> list:
    """ Identify Regions of Interest in the data based on a threshold criterion 
        applied to the standard deviation values (AccZ_sd)
        It filters out regions where the standard deviation is greater than or equal to twice 
        the threshold value (threshold * 2). These regions are stored in the filtered list along with their indices.

    Args:
        AccZ_sd: list with the all the regions that have a standad deviation greater or equal to twice the threshold
        
    Returns:
        list with the regions of interest
    """

    filtered = list()
    threshold: float = 0.5

    for i in range(len(AccZ_sd)):
        if AccZ_sd[i] >= threshold * 2:
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
    """ Count the number of identified regions of interest. Since the last region will always be
        the successful attempt, it substracts 1

    Args:
        regions_of_interest: list with the all the regions that have a standad deviation > our threshold

    Returns:
        int with Number of failed attempts
    """

    attempts = len(regions_of_interest) - 1

    return attempts
