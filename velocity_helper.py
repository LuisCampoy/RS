# Recovery Score Calculations: Velocity helper
# Script created 8/12/2024
# Last revision 8/15/2024

import pandas as pd
import numpy as np
from scipy.integrate import cumtrapz

def cal_vel(time, acceleration):
    """
    Calculate velocity from acceleration using numerical integration.
    
    Parameters:
    time : array-like
        The time data corresponding to each acceleration measurement.
    acceleration : array-like
        The acceleration data for which to calculate velocity.
        
    Returns:
    velocity : array-like
        The velocity calculated from the acceleration data.
    """
    # Calculate velocity using cumulative trapezoidal integration
    velocity = cumtrapz(acceleration, time, initial=0)
    
    return velocity


def add_vel(filtered_df):
    # Calculate velocity for each axis and create new DataFrame
    df = filtered_df
    df['Vel_X'] = cal_vel(df.iloc[:, 0], df['AccX'])
    df['Vel_Y'] = cal_vel(df.iloc[:, 0], df['AccY'])
    df['Vel_Z'] = cal_vel(df.iloc[:, 0], df['AccZ'])
 
    print('Velocity columns added to DataFrame successfully')
    
    return df


def get_auc_x(selected_data_list, time_list, acceleration_list, num_points) -> list[float]:
    """ Create a list with the calculation of the area under the curve (velocity)
        for each attempt 
        
    Args:
        selected_data_list: list with a list of dataframes. 
        One per event with three columns (AccX, AccY and AccZ)

    Returns:
        list [float64]
    """
    
    num_readings = len (selected_data_list)
    
    area = 0.0
    for i in range(1, num_points):
        dt = time_list[i] - time_list[i - 1]
        avg_acceleration = (acceleration_list[i] + acceleration_list[i - 1]) / 2.0
        area += avg_acceleration * dt
    return area

def get_auc_y():
    pass

def get_auc_z():
    pass



# Number of readings to store
num_readings = 10
time_readings = [0.0] * num_readings  # Initialize time readings list
acceleration_readings = [0.0] * num_readings  # Initialize acceleration readings list
index = 0
previous_time = time.time()

def read_acceleration():
    # Simulate reading acceleration (replace this with actual sensor data)
    # Example: return a random acceleration value between -10 and 10 m/s^2
    return random.uniform(-10, 10)

def calculate_area_under_curve(time_list, acceleration_list, num_points):
    area = 0.0
    for i in range(1, num_points):
        dt = time_list[i] - time_list[i - 1]
        avg_acceleration = (acceleration_list[i] + acceleration_list[i - 1]) / 2.0
        area += avg_acceleration * dt
    return area

while True:
    current_time = time.time()
    dt = current_time - previous_time
    previous_time = current_time

    # Simulate reading acceleration from a sensor (replace with actual sensor reading)
    acceleration = read_acceleration()

    if index < num_readings:
        time_readings[index] = time_readings[index - 1] + dt if index > 0 else dt
        acceleration_readings[index] = acceleration
        index += 1
    else:
        # Shift the readings to make space for the new one
        time_readings[:-1] = time_readings[1:]
        acceleration_readings[:-1] = acceleration_readings[1:]
        time_readings[-1] = time_readings[-2] + dt
        acceleration_readings[-1] = acceleration

    # Calculate the area under the curve using the trapezoidal rule
    area = calculate_area_under_curve(time_readings, acceleration_readings, index)

    # Print the result to the console
    print(f"Change in velocity: {area:.2f} m/s")

    
