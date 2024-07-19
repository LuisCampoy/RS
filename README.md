This script reads through a csv file.
It creates a window to scan the data. The window size is 'window_size' data points and the window is advancing every 'step_size' datapoints.
It calculates the standard deviation over a specified window size with a specified step size.
And then identifies the ‘Regions of Interest’ in the data based on a threshold criterion applied to the standard deviation values (AccZ_sd). It filters out regions where the standard deviation is greater than or equal to twice the threshold value (threshold * 2). 
Within each of these regions it calculates the maximum acceleration on each of the three axes, namely, X, Y and Z.
Based on these calculations, it provides:
•	The squared root (sqrt) of the sum of the squares of each max acceleration on each horizontal axis (AccX, AccY) for the successful attempt
•	The squared root (sqrt) of the sum of the squares of each max acceleration on the X and Y axes only for the successful attempt (this has a better R^2 value in the regression)
•	The squared root (sqrt) of the sum of the squares of each max acceleration on each axis (AccX, AccY, AccZ) for each of the unsuccessful attempt

Last revision: 5/29/2024
