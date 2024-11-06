import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np

# Read data from CSV file
data = pd.read_csv(r'c:\Users\thodi\Desktop\SMD3\Run3.csv')

# Extract the columns for time and angle data
time = data['Time (s)']
disk_angle = data['Disk Angle (rad)']
driver_angle = data['Driver Angle (rad)']

# Find peaks in both angle signals
disk_peaks, _ = find_peaks(disk_angle)
driver_peaks, _ = find_peaks(driver_angle)

# Initialize variables for phase differences
phase_diff_high_freq = None
phase_diff_resonance = None
phase_diff_low_freq = None

# High-Frequency (Near Time Zero) Phase Difference
if len(disk_peaks) > 0 and len(driver_peaks) > 0:
    # First peaks
    disk_first_peak = disk_peaks[0]
    driver_first_peak = driver_peaks[0]

    # Period T using the first two peaks of the disk angle
    if len(disk_peaks) > 1:
        T = time[disk_peaks[1]] - time[disk_peaks[0]]
    else:
        print("Not enough peaks found to calculate period.")
        T = None

    # Calculate high-frequency phase difference if T is defined
    if T:
        phase_diff_high_freq = 2 * np.pi * abs(time[disk_first_peak] - time[driver_first_peak]) / T
        print(f"High-Frequency Phase Difference: {phase_diff_high_freq:.4f} radians")

# Resonance Frequency Phase Difference (Maximum Amplitude of Disk Oscillation)
if T and len(disk_peaks) > 0:
    # Find the peak with the maximum amplitude in disk angle (resonance)
    resonance_peak = disk_peaks[np.argmax(disk_angle[disk_peaks])]
    
    # Find the closest driver peak to the resonance peak in time
    closest_driver_peak = min(driver_peaks, key=lambda i: abs(time[i] - time[resonance_peak]))
    
    # Calculate resonance phase difference
    phase_diff_resonance = 2 * np.pi * abs(time[resonance_peak] - time[closest_driver_peak]) / T
    print(f"Resonance Frequency Phase Difference: {phase_diff_resonance:.4f} radians")

# Low-Frequency (End of Interval) Phase Difference
if T and len(disk_peaks) > 0 and len(driver_peaks) > 0:
    # Last peaks in both signals
    disk_last_peak = disk_peaks[-1]
    driver_last_peak = driver_peaks[-1]
    
    # Calculate low-frequency phase difference
    phase_diff_low_freq = 2 * np.pi * abs(time[disk_last_peak] - time[driver_last_peak]) / T
    print(f"Low-Frequency Phase Difference: {phase_diff_low_freq:.4f} radians")

# Plotting the angle data
plt.figure(figsize=(10, 6))
plt.plot(time, disk_angle, label='Disk Angle (rad)', color='b')
plt.plot(time, driver_angle, label='Driver Angle (rad)', color='r')
plt.plot(time[disk_peaks], disk_angle[disk_peaks], 'bo', label='Disk Peaks')
plt.plot(time[driver_peaks], driver_angle[driver_peaks], 'ro', label='Driver Peaks')
plt.title('Disk and Driver Oscillations vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.legend()
plt.grid(True)
plt.show()