# RS: Main Script
# Script created 3/25/2024
# Last revision 5/29/2024

from operator import index
import pandas as pd

from file_helper import read_csv_file
from attempt_detection_helper import *
from region_helper import *
from acceleration_helper import *
from graph_helper import get_plot

def main() -> None:

    window_size: int = 10000
    step_size: int = 2000

    # file_path: str = input("Enter file name: ")
    file_path: str = "366647.csv"

    df: pd.DataFrame = read_csv_file(file_path)

    if df is not None:
        print("csv file red successfully.")
        #print(df.head())   
       
    AccZ_sd: list[float] = calculate_window_sd(df["AccZ"][1:], window_size, step_size)
    print('sd_list calculated succesfully')
    
    regions_of_interest: list = detect_regions_of_interest_Z(AccZ_sd)   
    print(regions_of_interest)
    print("Regions of Interest detected successfully...")

    number_of_failed_attempts: int = get_attempts(regions_of_interest)
    print(f"Number of Failed Attempts = {number_of_failed_attempts}")

    selected_data, selected_data_list = get_regions(df, regions_of_interest, window_size, step_size)
    print(selected_data)
    print('Data printed successfully')
    print(selected_data_list)
    print('Selected Data list')
       
    amax_x_list: list = get_max_accelerations_x(selected_data_list)
    print(f'amax_x_list is {amax_x_list}')
        
    amax_y_list: list = get_max_accelerations_y(selected_data_list)
    print(f'amax_y_list is {amax_y_list}')
    
    amax_z_list: list = get_max_accelerations_z(selected_data_list)
    print(f'amax_z_list is {amax_z_list}')
    
    sa: float = get_sa(amax_x_list, amax_y_list, amax_z_list)
    print(f'sa = {sa}')

    sa_2axes: float = get_sa_2axes(amax_x_list, amax_y_list)
    print(f'sa = {sa_2axes}')
    
    sumua: float = get_sumua(amax_x_list, amax_y_list, amax_z_list)
    
    
    #get_plot(df, regions_of_interest, window_size, step_size, file_path)

if __name__ == "__main__":
    main()
