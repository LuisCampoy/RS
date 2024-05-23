# RS: Main Script
# Script created  3/25/2024
# Last revision 5/23/2024

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
    file_path: str = "344717_RED.csv"

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

    selected_data_list, regions = get_regions(df, regions_of_interest, window_size, step_size)

    print(selected_data_list)
    print('Data printed successfully')
    
    print(regions[0])
    print('X region printed successfully')
    
    print(regions[1])
    print('Y region printed sucessfully')
    
    print(regions[2])
    print('Z region printed successfully')
    
   
     
    #amax = get_max_accelerations(regions)
    
    #print(f'max absolute acceleration in x, y and z are {amax}')
    
    
    
    # get_plot(df, regions_of_interest, window_size, step_size, file_path)

    #get_amax_sa(amax)

    
    # print('amax_sa printed sucessfully...')

    #amax_ua = get_amax_ua()


if __name__ == "__main__":
    main()
