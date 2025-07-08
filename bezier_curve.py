"""
Author: Lillian Olvera
Username: olverali01
Description: Generates a cubic Bézier curve for CAD applications.
"""

import numpy as np
import matplotlib.pyplot as plt

def bezier(t, points):
    return (1 - t)**3 * points[0] + 3*(1 - t)**2*t * points[1] + 3*(1 - t)*t**2 * points[2] + t**3 * points[3]

P = np.array([[0, 0], [1, 2], [3, 3], [4, 0]])
t = np.linspace(0, 1, 100)
curve = np.array([bezier(ti, P) for ti in t])

plt.plot(P[:, 0], P[:, 1], 'ro--', label='Control Points')
plt.plot(curve[:, 0], curve[:, 1], 'b-', label='Bezier Curve')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.title("Cubic Bézier Curve")
plt.show()
