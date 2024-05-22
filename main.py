# RS: Main Script
# Script created  3/25/2024
# Last revision 5/22/2024

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

        print("csv file returned to main() successfully")

    AccZ_sd: list[float] = calculate_window_sd(df["AccZ"][1:], window_size, step_size)
    """ Extracts a list of float values from df, 
        a dictionary, where "AccZ" is a key. [1:] starting from the second element

    Args:
        df (pd.DataFrame), window size (int), step_size (int)

    Returns:
        Pandas DataFrame (pd.DataFrame)
    """

    regions_of_interest = detect_regions_of_interest_Z(AccZ_sd)

    print(regions_of_interest)

    print("Regions of Interest detected successfully...")

    number_of_failed_attempts = get_attempts(regions_of_interest)

    print(f"Number of Failed Attempts = {number_of_failed_attempts}")

    get_region(df, regions_of_interest, window_size, step_size)

    print("ROI printed successfully...")

    # get_plot(df, regions_of_interest, window_size, step_size, file_path)

    get_amax_sa(df, regions_of_interest, window_size, step_size)

    
    # print('amax_sa printed sucessfully...')

    amax_ua = get_amax_ua()


if __name__ == "__main__":
    main()
