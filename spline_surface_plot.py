"""
Author: Lillian Olvera
Username: olverali01
Email: lillian.olvera@darlingii.com
Description: 3D B-spline surface approximation.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Define control points
x = np.random.rand(25) * 10
y = np.random.rand(25) * 10
z = np.sin(x / 2) + np.cos(y / 3)

# Create grid
xi = yi = np.linspace(0, 10, 100)
xi, yi = np.meshgrid(xi, yi)
zi = griddata((x, y), z, (xi, yi), method='cubic')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xi, yi, zi, cmap='viridis')
plt.title("B-Spline Surface")
plt.show()