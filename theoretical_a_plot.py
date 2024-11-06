import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Constants found numerically
delta = 0.02374
omega = 10.6458
v = 10.6428

# Establishing the time period we want the graph to find itself
t = np.linspace(0, 10, 1000)

# Define the function x(t)
x_t = np.exp(-delta * omega * t) * (0.0012 * np.sin(v * t) + 0.05 * np.cos(v * t))

# Find the peaks
peaks, _ = find_peaks(x_t)

# Do the actual plot x(t) against t
plt.figure(figsize=(8, 6))
plt.plot(t, x_t, label=r"$x(t) = e^{-\delta \omega t}\left(0.0012 \cdot \sin(vt) + 0.05 \cdot \cos(vt)\right)$")

# Highlight peaks with red dots for visual purposes
plt.plot(t[peaks], x_t[peaks], "ro", label="Peaks")

plt.title("Graph of $x(t)$ against $t$ in the time interval [0,10]s")
plt.xlabel("Time $t$")
plt.ylabel("$x(t)$")
plt.legend()
plt.grid(True)
plt.show()