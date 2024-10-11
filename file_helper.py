# Recovery Score Calculations: file_helper Script
# Script created  3/25/2024
# Last revision 10/9/2024

import pandas as pd
import numpy as np

def add_csv_extension(file_path: str) -> str:
    '''adds '.csv' to the file number

    Args:
        file_path (str): Case Number

    Returns:
        str: the Case Number (entered) plus the csv extension (.csv)
    '''

    file_path_csv: str = file_path + '.csv'

    return file_path_csv

def read_csv_file(file_path_csv) -> pd.DataFrame:
    '''Reads the first four columns (TimeStamp, AccX, AccY, AccZ) from the csv file
        using the read_csv function.
        skips the first row (Sep = ,)
        Uses the second row as header
        only reads the first 4 columns to speed up file reading time

    Args:
        file_path: cvs file's name

    Returns:
        Pandas DataFrame
    '''
    try:
        print('reading csv file...')

        df: pd.DataFrame = pd.read_csv(
            file_path_csv,
            skiprows = 3, # skip the first 3 rows (separator, headers, units)
            sep = ',',
            header = None, # No header in the remaining rows
            names = ['TimeStamp', 'AccX', 'AccY', 'AccZ'],
            usecols = [0, 1, 2, 3],
            dtype = {'TimeStamp': str, 'AccX': float, 'AccY': float, 'AccZ': float},
            encoding ='utf-8',
            low_memory = False,
        )
        
        # Convert 'TimeStamp' column to datetime format
        df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])
    
        return df

    except Exception as e:

        print("An error occurred:", str(e))
        
        return None 
 
def initial_filter(df: pd.DataFrame, target_value) -> pd.DataFrame:
    '''Filters initial csv file and creates a new df ignoring initial acceleration values.
       Looks into AccZ column (Z axis). Filters out initial values until it finds
       the first acceleration value on the Z axis that is greater than the 'target value'
       Identifies when horse gains sternal recumbency for the first time.
        
    Args:
        df (pd.DataFrame): first four columns of the initial csv file with formated timeStamp in column 0

    Returns:
        Pandas DataFrame: A new filtered DataFrame starting from when 'AccZ' exceeds the target value
    '''
    
    try:
   
        # Find the index of the first occurrence of the target value in column 'AccZ'
        start_index: int = df[df['AccZ'] > target_value].index[0]
        
        # Create the new DataFrame starting from that index
        filtered_df: pd.DataFrame = df.iloc[start_index:].reset_index(drop = True)
        
        return filtered_df
    
    except IndexError:
        # If the target value is not found, return the same dataFrame
        print(f'No values in "AccZ" greater than {target_value} could be found. Returning the original DataFrame')

        return df
    
def clean_data(df, target_value) -> pd.DataFrame:
    '''Cleans the AccZ column in a DataFrame by setting values lower than the threshold to NaN.
    
     Args:
        df (pandas.DataFrame): The input DataFrame that contains an 'AccZ' column.
        target_value (float): The threshold below which values are considered invalid.
    
    Returns:
    pandas.DataFrame: The cleaned DataFrame with values below the threshold set to NaN.
    '''
    # Ensure the AccZ column exists
    if 'AccZ' in df.columns:
        df['AccZ'] = df['AccZ'].apply(lambda x: x if x >= target_value else np.nan)

    else:
        raise KeyError('The "AccZ" column is not present in the DataFrame.')
    
    return df



    