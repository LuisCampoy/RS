# Recovery Score Calculations: Acceleration helper
# Script created  3/25/2024
# Last revision 5/28/2024

import pandas as pd

def get_max_accelerations(regions)->list[float]:
    """Create a list with the maximum absolute values foe each region of interest and for each column (AccX, AccY, AccZ)

    Args:
        regions:

    Returns:
        list [float64]

    """
    #raise NotImplementedError("Sorry, get_amax_accels is not implemented yet...")
    amax = []
    amax_x: float = regions[1].abs().max()
    amax_y: float = regions[2].abs().max()
    amax_z: float = regions[3].abs().max()
    amax = [amax_x, amax_y, amax_z]
    
    return amax

def get_amax_sa(amax_x_region, amax_y_region):
    """Create a new pd.DataFrafe with the 2 columns (AccX, AccY) within the last region of interest (successful attempt)
        Creat start index and end index from...???
        Calculate abs value of each colum and then return the max value from each column

    Args:
        df:
        regions_of_interest:
        window_size:
        step_size:

    Returns:
        list

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

    