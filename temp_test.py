"""
Plot magnetization vs temperature for fixed lattice size.
Run ensembles of different temperatures, average results.
"""
import numpy as np
from ising_2d import ising_2d
import matplotlib.pyplot as plt

LATTICE_SIZE = 32
TEMPERATURES = np.linspace(1.0, 4.0, 20)

temperature_average_magnetizations = []

for T in TEMPERATURES:
    ensemble_average_magnetizations = []
    for _ in range(100):
        magnetization = ising_2d(LATTICE_SIZE, T, sweeps=1000, burn_in=200)
        ensemble_average_magnetizations.append(magnetization)
        print(f'T={T:.2f}, Magnetization={magnetization:.4f}')
    avg_magnetization = np.mean(ensemble_average_magnetizations)
    temperature_average_magnetizations.append(avg_magnetization)

plt.plot(TEMPERATURES, temperature_average_magnetizations, marker='o')
plt.xlabel('Temperature (T)')
plt.ylabel('Average Magnetization')
plt.title(f'2D Ising Model: L={LATTICE_SIZE}')
plt.grid()
plt.savefig('magnetization_vs_temperature.png')