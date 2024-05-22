# Recovery Score Calculations: Calculation helper
# Script created  3/25/2024
# Last revision 5/22/2024

import pandas as pd

# calculate maximum absolute value within the ROI in X, Y and Z axis
def get_regions(df, regions_of_interest, window_size, step_size):
    
    selected_data = [] 
    
    #loop through each ROI
    for i in range(len(regions_of_interest)):
        
        start_index = regions_of_interest[i][0] * step_size
        end_index = start_index + window_size

        # Select rows using iloc and columns using column names
        selected_data = df.iloc[start_index:end_index][['AccX', 'AccY', 'AccZ']]
        
        print(
            'ROI ',
            i + 1,
            ': (',
            df['TimeStamp'][regions_of_interest[i][0] * step_size],
            ',',
            df['TimeStamp'][regions_of_interest[i][0] * step_size + window_size],
            ')',
        )
    
        print(selected_data)
        
        amax = selected_data.max()
        
        print(f'Amax is {amax}')
        
    
    print('selected_data printed sucessfully...')
    print('ROI printed successfully...')
    
    return amax
    
    
   
    
    

        
              
      