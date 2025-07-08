"""
Author: Lillian Olvera
Username: olverali01
Description: Calculates follower displacement based on harmonic cam motion.
"""

import numpy as np
import matplotlib.pyplot as plt

angle = np.linspace(0, 2*np.pi, 360)
lift = 10  # mm
displacement = lift * (1 - np.cos(angle)) / 2

plt.plot(np.degrees(angle), displacement)
plt.title("Harmonic Cam Follower Displacement")
plt.xlabel("Cam Angle (degrees)")
plt.ylabel("Follower Displacement (mm)")
plt.grid(True)
plt.show()