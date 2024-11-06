import pandas as pd
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv(r'C:\Users\thodi\Desktop\SMD3\Group 14 - 1, damped(Group 14 - 1, damped).csv')
data.columns = ['Time (s)', 'Pulley Movement (cm)']

# Filter data to start from 10.5 seconds onwards
filtered_data = data[data['Time (s)'] >= 7.5 ]


# Find peaks in the displacement data
peaks, _ = find_peaks(filtered_data['Pulley Movement (cm)'])

# Ensure there are enough peaks found
if len(peaks) > 3:
    # Extract the time and displacement values, but ignore the first three peaks
    peak_times_after_third = filtered_data['Time (s)'].iloc[peaks[3:]].values
    peak_values_after_third = filtered_data['Pulley Movement (cm)'].iloc[peaks[3:]].values
    
    # Plot displacement vs. time
    plt.figure(figsize=(10, 6))
    plt.plot(filtered_data['Time (s)'], filtered_data['Pulley Movement (cm)'], label="Pulley Movement")
    
    # Highlight peaks with red dots, excluding the first three peaks
    plt.scatter(peak_times_after_third, peak_values_after_third, color='red', label='Peaks', zorder=5)
    plt.title('Pulley Movement vs. Time for an Undamped Oscillator')
    plt.xlabel('Time (s)')
    plt.ylabel('Pulley Movement (cm)')
    plt.grid(True)
    plt.legend()
    plt.show()
    
    # Calculate the differences between successive peaks (periods)
    periods = np.diff(peak_times_after_third)
    
    # Calculate the mean period and frequency
    mean_period = np.mean(periods)
    oscillation_frequency = 2 * np.pi / mean_period if mean_period > 0 else 0
    
    # Output the results
    print(f'Mean Period (after first 3 peaks): {mean_period:.4f} seconds')
    print(f'Oscillation Frequency (after first 3 peaks): {oscillation_frequency:.4f} rad/s')
