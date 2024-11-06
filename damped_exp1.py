import pandas as pd
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv(r'C:\Users\thodi\Desktop\SMD3\Group 14 - 1, damped(Group 14 - 1, damped).csv')
data.columns = ['Time (s)', 'Pulley Movement (cm)']

# Find peaks in the displacement data
peaks, _ = find_peaks(data['Pulley Movement (cm)'])

# Ensure that peaks are found
if len(peaks) > 0:
    # Extract the displacement values at the peaks
    peak_values = data['Pulley Movement (cm)'].iloc[peaks].values
    
    # Find the index of the maximum peak (highest y value)
    max_peak_index = peaks[np.argmax(peak_values)]
    
    # Filter the data starting from the maximum peak
    data_after_max_peak = data.iloc[max_peak_index:]
    
    # Extract the time values and displacement values after the maximum peak
    peak_times_after_max = data['Time (s)'].iloc[peaks[peaks >= max_peak_index]].values
    peak_values_after_max = data['Pulley Movement (cm)'].iloc[peaks[peaks >= max_peak_index]].values

    # Plot displacement vs. time starting from the maximum peak
    plt.figure(figsize=(10, 6))
    plt.plot(data_after_max_peak['Time (s)'], data_after_max_peak['Pulley Movement (cm)'], label="Pulley Movement")

    # Highlight peaks with red dots after the maximum peak
    plt.scatter(peak_times_after_max, peak_values_after_max, color='red', label='Peaks', zorder=5)

    plt.title('Pulley Movement vs. Time for a Damped Oscillator')
    plt.xlabel('Time (s)')
    plt.ylabel('Pulley Movement (cm)')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Calculate the differences between successive peaks (periods)
    periods = np.diff(peak_times_after_max)

    # Calculate the mean period and frequency
    mean_period = np.mean(periods)
    oscillation_frequency = 2*np.pi / mean_period if mean_period > 0 else 0

    # Output the results
    print(f'Mean Period: {mean_period:.4f} seconds')
    print(f'Oscillation_Frequency: {oscillation_frequency:.4f} rad/s')