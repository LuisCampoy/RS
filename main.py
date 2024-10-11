# RS: Main Script
# Script created 3/25/2024
# Last revision 10/11/2024

#from pickle import NONE
import pandas as pd
from datetime import datetime

from acceleration_helper import get_max_accelerations_x, get_max_accelerations_y, get_max_accelerations_z, get_sa_2axes, get_sumua
from attempt_detection_helper import calculate_window_sd, detect_regions_of_interest_Z, get_attempts
from file_helper import read_csv_file, add_csv_extension, initial_filter, clean_data
from graph_helper import get_plot
from region_helper import get_regions
from output_results_helper import process_recovery
#from velocity_helper import get_auc_x, get_auc_y, get_auc_z

def main() -> None:
   
    start_time: str = datetime.now().strftime('%Y-%m-%d_%H.%M')

    # values that can be changed  to increase/ decrease sensitivity
    window_size: int = 10000 # each cell is 5ms. 10000 cells represent 2secs
    step_size: int = 2000 # 2000 cells are 400ms (0.4secs)
    target_value: float = 9.9 # acceleration value
    threshold: float = 1.5 # threshold for SD

    file_path: str = input('Enter file name: ')
    file_path_csv: str = add_csv_extension(file_path)
    
    df: pd.DataFrame = read_csv_file(file_path_csv)

    if df is not None:
        print('File read successfully...')
        
    else:
        print('Failed to load DataFrame')
        return # exit if the file cannot be loaded
        
    # Create new df in which Z values are ignored until Z values reach target_value 
    # corresponding with horse getting onto sternal recumbency
    df_filtered: pd.DataFrame = initial_filter(df, target_value)
    # I will eventually remove the initial filtyer and leave this one...
    df_cleaned: pd.DataFrame = clean_data(df_filtered, target_value)

    while True:
        AccZ_sd: list[float] = calculate_window_sd(df_cleaned["AccZ"][1:], window_size, step_size)
        print('sd_list calculated succesfully')
        #print(f'Accz_sd is {AccZ_sd}')
        
        regions_of_interest: list[float] = detect_regions_of_interest_Z(AccZ_sd, threshold)   
        print('Regions of Interest detected successfully')
        #print(f'Regions of interest {regions_of_interest}')
    
        get_plot(df_cleaned, regions_of_interest, window_size, step_size, file_path) 
        
        redo: str = input('continue or re calculate with different threshold? (C/R) ').lower()

        if redo == 'c':
                
            # Process and calculate data based on initial default parameters for threshold
            number_of_failed_attempts: int = get_attempts(regions_of_interest)
            #print(f'Number of Failed Attempts = {number_of_failed_attempts}')

            selected_data_list:list = get_regions(df_cleaned, regions_of_interest, window_size, step_size)
            #print(selected_data)
            #print('Data printed successfully')
            #print(selected_data_list)
            #print('Selected Data list')
                
            amax_x_list: list[float] = get_max_accelerations_x(selected_data_list)
            #print(f'amax_x_list is {amax_x_list}')
                    
            amax_y_list: list[float] = get_max_accelerations_y(selected_data_list)
            #print(f'amax_y_list is {amax_y_list}')
                
            amax_z_list: list[float] = get_max_accelerations_z(selected_data_list)
            #print(f'amax_z_list is {amax_z_list}')
                
            #sa: float = get_sa(amax_x_list, amax_y_list, amax_z_list)
            #print(f'sa = {sa}')

            sa_2axes: float = get_sa_2axes(amax_x_list, amax_y_list)
            #print(f'sa_2axes = {sa_2axes}')
                
            sumua:float = get_sumua(amax_x_list, amax_y_list, amax_z_list)
            #print(f'ua_list = {ua_list}')
            #print(f'sumua = {sumua}')
                
            '''
            velocity_x = get_auc_x(time_readings, acceleration_readings, index)
            velocity_y = get_auc_y
            velocity_z = get_auc_z
            '''  
            rs_2axes_py: float = process_recovery(file_path, number_of_failed_attempts, sa_2axes, sumua)

            # output_results: pd.DataFrame = get_output_results(file_path, number_of_failed_attempts, sa_2axes, sumua)
            print(f'results are')
            print(f'file name: {file_path}')
            print(f'Number of failed attempts: {number_of_failed_attempts}')
            print(f'sa_2axes= {sa_2axes}')
            print(f'sumua= {sumua}')
            print(f'rs_2axes_py= {rs_2axes_py}')
    
            break # exit loop after processing results

        elif redo == 'r':
         # Set a new value for Threshold
            try:
                recalibrate_threshold_str: str = input('Enter new threshold ')
                recalibrate_threshold: float = float(recalibrate_threshold_str)
                threshold: float = recalibrate_threshold
                print(f'Threshold recalibrated to {threshold}')

            except ValueError:
                print('invalid entry. Enter a float value')
        
        else:
            print('invalid option. Enter either "c" to continue or "r" to recalibrate')

if __name__ == "__main__":
    
    main()