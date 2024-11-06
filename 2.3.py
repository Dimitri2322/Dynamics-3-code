import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np

# Read data from CSV
data = pd.read_csv(r'C:\Users\thodi\Desktop\SMD3\Run 1.csv')

# Access the specific columns for Time and Angular Displacement
time = data['Time (s)']
angular_displacement = data['Disk Angle (rad)']

# Filter data to start from 2 seconds
filtered_data = data[data['Time (s)'] >= 2]

# Access filtered time and angular displacement
time = filtered_data['Time (s)']
angular_displacement = filtered_data['Disk Angle (rad)']

# Define the region where the data flattens out (e.g., last 10% of the data)
flattened_region = angular_displacement[-int(0.1 * len(angular_displacement)):]

# Calculate the offset as the mean of the flattened region
offset = np.mean(flattened_region)

# Account for the offset by subtracting it from the angular displacement data
adjusted_angular_displacement = angular_displacement - offset

# Plot the adjusted data
plt.figure(figsize=(10, 6))
plt.plot(time, adjusted_angular_displacement, label='Adjusted Disk Angular Displacement', color='b', marker='o')
plt.xlabel('Time (s)')
plt.ylabel('Angular Displacement (rad)')
plt.title('Shifted Down Disk Angular Displacement as a Function of Time')
plt.legend()
plt.grid(True)
plt.show()

# Identify peaks and calculate the average time period as before
interval_mask = (time >= 5) & (time <= 20)
time_interval = time[interval_mask]
adjusted_displacement_interval = adjusted_angular_displacement[interval_mask]

peaks, _ = find_peaks(adjusted_displacement_interval)
peak_times = time_interval.iloc[peaks].values
time_diffs = np.diff(peak_times)
average_time_period = np.mean(time_diffs)

print("Offset:", offset)
print("Average Time Period after Offset Adjustment:", average_time_period)