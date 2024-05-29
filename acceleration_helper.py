# Recovery Score Calculations: Acceleration helper
# Script created 3/25/2024
# Last revision 5/29/2024

from numpy import sqrt
import pandas as pd

def get_max_accelerations_x(selected_data_list) -> list[float]:
    """ Create a list with the maximum absolute values for each attempt 
        for 'AccX'

    Args:
        selected_data_list: list with a list of dataframes. 
        One per event with three columns (AccX, AccY and AccZ)

    Returns:
        list [float64]

    """
   
    amax_x_list = []
        
    for i in range (len (selected_data_list)):
        amax_x = selected_data_list[i]['AccX'].abs().max()
        amax_x_list.append(amax_x)
    
    return amax_x_list

def get_max_accelerations_y(selected_data_list) -> list[float]:
    """ Create a list with the maximum absolute values for each attempt 
        for 'AccY'

    Args:
        selected_data_list: list with a list of dataframes. 
        One per event with three columns (AccX, AccY and AccZ)

    Returns:
        list [float64]

    """
   
    amax_y_list = []
        
    for i in range (len (selected_data_list)):
        amax_y = selected_data_list[i]['AccY'].abs().max()
        amax_y_list.append(amax_y)
    
    return amax_y_list
        
def get_max_accelerations_z(selected_data_list) -> list[float]:
    """ Create a list with the maximum absolute values for each attempt 
        for 'AccZ'

    Args:
        selected_data_list: list with a list of dataframes. 
        One per event with three columns (AccX, AccY and AccZ)

    Returns:
        list [float64]

    """
   
    amax_z_list = []
        
    for i in range (len (selected_data_list)):
        amax_z = selected_data_list[i]['AccZ'].abs().max()
        amax_z_list.append(amax_z)
    
    return amax_z_list

def get_sa(amax_x_list, amax_y_list, amax_z_list) -> float:
    """ Calculate the squared root (SQRT) of the sum of the squares 
        of each max acceleration on each axis (AccX, AccY, AccZ)
        for the successful attempt

    Args:
        amax_x_list: list with the max absolute accelerations on AccX per event.
                    last argument of this list is the succesful attempt
        amax_y_list: list with the max absolute accelerations on AccY per event.
                    last argument of this list is the succesful attempt
        amax_z_list: list with the max absolute accelerations on AccZ per event.
                    last argument of this list is the succesful attempt
        
    Returns:
        float

    """
    
    i = len(amax_z_list)-1
    sa = sqrt(amax_x_list[i] ** 2  + amax_y_list[i] ** 2 + amax_z_list[i] ** 2)
    
    return sa     
    
def get_sa_2axes(amax_x_list, amax_y_list) -> float:
    """ Calculate the squared root (SQRT) of the sum of the squares 
        of each max acceleration on the X and Y axes only for the successful attempt.

    Args:
        amax_x_list: list with the max absolute accelerations on AccX per event.
                    last argument of this list is the succesful attempt
        amax_y_list: list with the max absolute accelerations on AccY per event.
                    last argument of this list is the succesful attempt
         
    Returns:
        float

    """
       
    i = len(amax_x_list)-1
    sa_2axes = sqrt(amax_x_list[i] ** 2  + amax_y_list[i] ** 2)
    
    return sa_2axes

def get_sumua(amax_x_list, amax_y_list, amax_z_list):
    """ Calculate the squared root (SQRT) of the sum of the squares 
        of each max acceleration on each axis (AccX, AccY, AccZ)
        for each of the the unsuccessful attempts

    Args:
        amax_x_list: list with the max absolute accelerations on AccX per event.
                    last argument of this list is the succesful attempt
        amax_y_list: list with the max absolute accelerations on AccY per event.
                    last argument of this list is the succesful attempt
        amax_z_list: list with the max absolute accelerations on AccZ per event.
                    last argument of this list is the succesful attempt
        
    Returns:
        float

    """
    #raise NotImplementedError('function not implemented yet...')

    ua_list = []
    
    for i in range (len (amax_z_list)-1):
        
        ua: float = sqrt(amax_x_list[i] ** 2  + amax_y_list[i] ** 2 + amax_z_list[i] ** 2)
        ua_list.append(ua)
        
    sumua: float = sum(ua_list)
   
    return ua_list, sumua