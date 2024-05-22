# Recovery Score Calculations: Calculation helper
# Script created  3/25/2024
# Last revision 5/22/2024

import pandas as pd

# calculate maximum absolute value within the ROI in X, Y and Z axis
def get_region(df, regions_of_interest, window_size, step_size):

    for j in range(len(regions_of_interest)):
        print(
            'ROI ',
            j + 1,
            ': (',
            df['TimeStamp'][regions_of_interest[j][0] * step_size],
            ',',
            df['TimeStamp'][regions_of_interest[j][0] * step_size + window_size],
            ')',
        )
              
      