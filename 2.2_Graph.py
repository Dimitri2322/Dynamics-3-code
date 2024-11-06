import numpy as np
import matplotlib.pyplot as plt

# Given constants
theta_o = 0.362
I = 0.0001341
omega_forcing = np.linspace(0,20,500)
omega_natural = 4.394
b = 9.68e-5
k_eq = 0.00259
tau_o = k_eq*theta_o


# Calculate theta using the given formula
theta_value = (tau_o / I) / (np.sqrt((omega_forcing**2 - omega_natural**2)**2 + (b / I)**2 * omega_forcing**2))
plt.plot(omega_forcing,theta_value)
plt.xlabel('Forcing Frequency')
plt.ylabel('Theta')
plt.title('Angular Displacement as a Function of the Forcing Frequency')
plt.grid(True)
plt.show()