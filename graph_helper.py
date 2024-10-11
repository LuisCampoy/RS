# Recovery Score Calculations: Graph_Helper Script
# Script created  3/25/2024
# Last revision 10/9/2024

from types import NoneType
import matplotlib.pyplot as plt

def get_plot(df, regions_of_interest, window_size, step_size, file_path) -> None:
    '''Creates a plot of the Z axis only with the detected Regions of Interest
    
    Args:
        df: list with the all the regions that have a standad deviation greater or equal to our threshold
        regions_of_interest:
        window_size:
        step_size:
        file_path:

    Returns:
        None
    '''
    
    plt.figure(figsize=(10, 6))
    plt.plot(
    df['TimeStamp'][0:],
    df['AccX'][0:],
    label= "AccX",
    )
    plt.plot(
    df['TimeStamp'][0:],
    df['AccY'][0:],
    label= 'AccY',
    )
    plt.plot(
    df['TimeStamp'][0:],
    df['AccZ'][0:],
    label= 'AccZ',
    )

    for k in range(len(regions_of_interest)):
        plt.vlines(
            df['TimeStamp'][regions_of_interest[k][0] * step_size],
            -30,
            30,
            colors= 'r',
            linestyles= 'dashed',
            label= 'ROI',
        )

        plt.vlines(
            df['TimeStamp'][regions_of_interest[k][0] * step_size + window_size],
            -30,
            30,
            colors=  'r',
            linestyles= 'dashed',
        )
    plt.xlabel('TimeStamp')
    plt.ylabel('Accelerations (m/s^2)')
    plt.title(file_path)
    plt.grid(which='both')
    plt.legend()
    plt.show()
    
