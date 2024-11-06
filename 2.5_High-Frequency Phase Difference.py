import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np

# Read data from CSV file
data = pd.read_csv(r'C:\Users\thodi\Desktop\SMD3\Run3.csv')

# Access the specific columns for Disk and Driver Angular Velocity
time = data['Time (s)']
disk_angular_velocity = data['Disk Angular Velocity (rad/s)']
driver_angular_velocity = data['Driver Angular Velocity (rad/s)']

# Find peaks in both signals
disk_peaks, _ = find_peaks(disk_angular_velocity)
driver_peaks, _ = find_peaks(driver_angular_velocity)

# Filter data for the time interval [0, 10] seconds
mask = (time >= 0) & (time <= 10)
time_0_10 = time[mask]
disk_angular_velocity_0_10 = disk_angular_velocity[mask]
driver_angular_velocity_0_10 = driver_angular_velocity[mask]

# Calculate the period T using the first two peaks of the disk signal
if len(disk_peaks) > 1:
    T = time[disk_peaks[1]] - time[disk_peaks[0]]
else:
    print("Not enough peaks found to calculate period.")
    T = None

# Calculate Phase Difference at t = 0s
phase_diff_0s = None
if T:
    disk_first_peak = disk_peaks[0]
    driver_first_peak = driver_peaks[0]

    phase_diff_0s = 2 * np.pi * abs(time[driver_first_peak] - time[disk_first_peak]) / T
    print(f"High Frequency Phase Difference at t = 0s: {phase_diff_0s:.4f} radians")

# Plotting for 0 to 10 seconds
plt.figure(figsize=(10, 6))
plt.plot(time_0_10, disk_angular_velocity_0_10, label='Disk Angular Velocity (rad/s)', color='b')
plt.plot(time_0_10, driver_angular_velocity_0_10, label='Driver Angular Velocity (rad/s)', color='r')
plt.plot(time_0_10[disk_peaks[time[disk_peaks] <= 10]], 
         disk_angular_velocity_0_10[disk_peaks[time[disk_peaks] <= 10]], 'bo', label='Disk Peaks')
plt.plot(time_0_10[driver_peaks[time[driver_peaks] <= 10]], 
         driver_angular_velocity_0_10[driver_peaks[time[driver_peaks] <= 10]], 'ro', label='Driver Peaks')
plt.title('Disk and Driver Angular Velocity (0 to 10 seconds)')
plt.xlabel('Time (s)')
plt.ylabel('Angular Velocity (rad/s)')
plt.legend()
plt.grid(True)
plt.xlim(0, 10)
plt.show()