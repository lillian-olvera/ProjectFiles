"""
Author: Lillian Olvera
Username: olverali01
Email: lillianolvera@namengineering.darlingii.com
Description: Plots modal analysis frequency response.
"""

import numpy as np
import matplotlib.pyplot as plt

freq = np.linspace(0, 500, 1000)
response = 1 / np.sqrt((1 - (freq/200)**2)**2 + (2*0.05*(freq/200))**2)

plt.plot(freq, response)
plt.title("Modal Frequency Response")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
