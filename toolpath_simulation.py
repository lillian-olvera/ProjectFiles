"""
Author: Lillian Olvera
Username: olverali01
Description: Simulates a basic CNC toolpath for a circular pocket.
"""

import matplotlib.pyplot as plt
import numpy as np

r = 10
turns = 5
theta = np.linspace(0, 2*np.pi*turns, 1000)
x = (r - theta / (2*np.pi)) * np.cos(theta)
y = (r - theta / (2*np.pi)) * np.sin(theta)

plt.plot(x, y)
plt.title("Simulated Spiral Toolpath")
plt.axis('equal')
plt.grid(True)
plt.show()