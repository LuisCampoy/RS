# RS: Main Script
# Script created 3/25/2024
# Last revision 7/17/2024

import pandas as pd
from datetime import datetime

from file_helper import *
from attempt_detection_helper import *
from region_helper import *
from acceleration_helper import *
from graph_helper import get_plot
from recovery_score_helper import *
from save_data_helper import *

def main() -> None:
   
    # Generate a timestamp for the backup file
    start_time: str = datetime.now().strftime('%Y-%m-%d_%H.%M')
       
    window_size: int = 10000
    step_size: int = 2000

    file_path: str = input('Enter file name: ')
       
    df: pd.DataFrame = read_csv_file(file_path)

    if df is not None:
        print('csv file read successfully.')
        
    else:
        print('Failed to load DataFrame')
        
    # Create new df in which Z values are ignored until Z values reach target_value (~9.8) 
    # corresponding with horse getting onto sternal recumbency
    filtered_df: pd.DataFrame = initial_filter(df)

    AccZ_sd: list[float] = calculate_window_sd(filtered_df["AccZ"][1:], window_size, step_size)
    print('sd_list calculated succesfully')
    #print(f'Accz_sd is {AccZ_sd}')
    
    regions_of_interest: list[float] = detect_regions_of_interest_Z(AccZ_sd)   
    print('Regions of Interest detected successfully')
    print(f'Regions of interest {regions_of_interest}')
   
    number_of_failed_attempts: int = get_attempts(regions_of_interest)
    print(f'Number of Failed Attempts = {number_of_failed_attempts}')

    selected_data, selected_data_list = get_regions(filtered_df, regions_of_interest, window_size, step_size)
    print(selected_data)
    print('Data printed successfully')
    print(selected_data_list)
    print('Selected Data list')
       
    amax_x_list: list = get_max_accelerations_x(selected_data_list)
    print(f'amax_x_list is {amax_x_list}')
        
    amax_y_list: list = get_max_accelerations_y(selected_data_list)
    #print(f'amax_y_list is {amax_y_list}')
    
    amax_z_list: list = get_max_accelerations_z(selected_data_list)
    #print(f'amax_z_list is {amax_z_list}')
    
    sa: float = get_sa(amax_x_list, amax_y_list, amax_z_list)
    #print(f'sa = {sa}')

    sa_2axes: float = get_sa_2axes(amax_x_list, amax_y_list)
    #print(f'sa_2axes = {sa_2axes}')
    
    ua_list, sumua = get_sumua(amax_x_list, amax_y_list, amax_z_list)
    #print(f'ua_list = {ua_list}')
    #print(f'sumua = {sumua}')
    
    data_to_save: pd.DataFrame = create_pd_df(number_of_failed_attempts, sa, sa_2axes, sumua)
    #print('data_to_save are')
    print(data_to_save)
    
    file_path_to_save: str = rename(file_path)
    #print(f'new name for the file is: {file_path_to_save}')
    
    #get_plot(df, regions_of_interest, window_size, step_size, file_path)
    get_plot(filtered_df, regions_of_interest, window_size, step_size, file_path)
    
    save_data(file_path_to_save, data_to_save, start_time)
    
    if number_of_failed_attempts >= 1:
        
        recovery_score_ua = get_rs_ua(sa_2axes, sumua)
                
    else:
        recovery_score_sa = get_rs_sa(sa_2axes)  
 
if __name__ == "__main__":
    
    main()