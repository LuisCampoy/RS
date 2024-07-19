# Recovery Score Calculations: file_helper Script
# Script created  3/25/2024
# Last revision 7/17/2024

import pandas as pd

def read_csv_file(file_path) -> pd.DataFrame:
    '''Read the first four columns (TimeStamp, AccX, AccY, AccZ) from the csv file
        using the read_csv function.
        skips the first row (Sep = ,)
        Uses the second row as header
        only reads the first 4 rows to speed file reading time

    Args:
        file_path: cvs file's name

    Returns:
        Pandas DataFrame
    '''
    try:
        print('reading csv file...')

        df: pd.DataFrame = pd.read_csv(
            file_path,
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
  
def initial_filter(df) -> pd.DataFrame:
    '''filters initial csv file and creates a new df ignoring initial values.
       Looks into AccZ column (Z axis). Filters out initial values until finds
       the first acceleration value on the Z axis that is greater than the 'target value'
       Identifies when horse gains sternal recumbency for the first time
        
    Args:
        df: first four columns of the initial csv file with formated timeStamp in column 0

    Returns:
        Pandas DataFrame
    '''
    # Define the target value
    target_value = 10 # threshold for acceleration seen on Z axis once horse is in sternal recumbency

    try:
   
        # Find the index of the first occurrence of the target value in column 'AccZ'
        start_index: int = df[df['AccZ'] > target_value].index[0]
        
        # Create the new DataFrame starting from that index
        filtered_df: pd.DataFrame = df.iloc[start_index:].reset_index(drop = True)
        
        return filtered_df
    
    except IndexError:
        # If the target value is not found, return the same dataFrame
        
        return df
