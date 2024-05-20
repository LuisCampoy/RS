# Recovery Score Calculations: Graph_Helper Script
# Script created  3/25/2024
# Last revision 5/19/2024

from types import NoneType
import matplotlib.pyplot as plt

def get_plot(df, regions_of_interest, window_size, step_size, file_path) -> None:
    """Create a plot of the Z axis only with the detected Regions of Interest
    
    Args:
        result: list with the all the regions that have a standad deviation greater or equal to our threshold
        regions_of_interest:
        window_size:
        step_size:
        file_path:

    Returns:
        None
    """
    plt.plot(
    df['Shimmer_4DA1_TimestampSync_FormattedUnix_CAL'][1:],
    df['Shimmer_4DA1_Accel_LN_X_CAL'][1:],
    label="AccX",
    )
    plt.plot(
    df['Shimmer_4DA1_TimestampSync_FormattedUnix_CAL'][1:],
    df['Shimmer_4DA1_Accel_LN_Y_CAL'][1:],
    label='AccY',
    )
    plt.plot(
    df["Shimmer_4DA1_TimestampSync_FormattedUnix_CAL"][1:],
    df["Shimmer_4DA1_Accel_LN_Z_CAL"][1:],
    label="AccZ",
    )

    for k in range(len(regions_of_interest)):
        plt.vlines(
            df["Shimmer_4DA1_TimestampSync_FormattedUnix_CAL"][regions_of_interest[k][0] * step_size
            ],
            -30,
            30,
            colors="r",
            linestyles="dashed",
            label="ROI",
        )

        plt.vlines(
            df["Shimmer_4DA1_TimestampSync_FormattedUnix_CAL"][
                regions_of_interest[k][0] * step_size + window_size
            ],
            -30,
            30,
            colors="r",
            linestyles="dashed",
        )

    plt.xlabel("Shimmer_4DA1_TimestampSync_FormattedUnix_CAL")
    plt.ylabel("Accelerations (m/s^2)")
    plt.title(file_path)
    plt.grid(which="both")
    plt.legend()
    plt.show()