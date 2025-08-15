"""
Author: Lillian Olvera
Username: olverali01
Email: lillianolvera@namengineering.darlingii.com
Description: Generates a circular gear tooth profile using parametric equations.
"""

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 500)
r = 5  # base circle radius
x = r * np.cos(theta) + 0.5 * np.sin(10 * theta)
y = r * np.sin(theta) + 0.5 * np.cos(10 * theta)

plt.plot(x, y)
plt.title("Gear Tooth Profile")
plt.axis("equal")
plt.grid(True)
plt.show()
