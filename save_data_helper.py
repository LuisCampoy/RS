# Recovery Score Calculations: save_data_helper Script
# Script created  5/30/2024
# Last revision 6/26/2024

import os
import pandas as pd

def create_pd_df(number_of_failed_attempts, sa, sa_2axes, sumua)-> pd.DataFrame:
    
    data = {
        'number_of_failed_attempts' : [number_of_failed_attempts],
        'sa' : [sa],
        'sa_2axes' : [sa_2axes],
        'sumua' : [sumua]
    }
    
    df = pd.DataFrame(data)
    
    return df

def rename(file_path) -> str:
    
    #raise NotImplementedError ('function not implemented yet...')
    #remove '.csv'
    
    file_path_to_save = file_path.replace('.csv', '')   
    
    return file_path_to_save

def save_data(file_path_to_save, data_to_save, start_time)-> None:
    
    x: str = input('do you want to save the file? (y/n) ')
    
    if x == 'y':
        
        tempname: str =  f'{file_path_to_save}_{start_time}.csv'
        #print(f'tempname is: {tempname}')
        data_to_save.to_csv(f'{tempname}', mode = 'a', index = False, header = True)
        print('data file saved')
        
    else:
        print('program terminated, good bye')