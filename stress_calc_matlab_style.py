"""
Author: Lillian Olvera
Username: olverali01
Description: Calculates stress using force and area - MATLAB style syntax.
"""

def stress(force, area):
    return force / area

F = 1000  # N
A = 50    # mm^2
sigma = stress(F, A)
print(f"Stress: {sigma:.2f} N/mm^2")