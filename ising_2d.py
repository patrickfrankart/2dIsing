import numpy as np
def ising_2d(L, T, sweeps, burn_in):
    spins = np.random.choice([-1, 1], size=(L, L))

    def delta_energy(i, j):
        s = spins[i, j]
        neighbors = (
            spins[(i + 1) % L, j] +
            spins[(i - 1) % L, j] +
            spins[i, (j + 1) % L] +
            spins[i, (j - 1) % L]
        )
        return 2 * s * neighbors
    
    magnetizations = []

    for sweep in range(sweeps):
        for _ in range(L * L):
            i = np.random.randint(L) 
            j = np.random.randint(L)
            dE = delta_energy(i, j)
            if dE <= 0 or np.random.rand() < np.exp(-dE / T):
                spins[i, j] *= -1
        
        if sweep >= burn_in:
            magnetizations.append(abs(spins.mean()))

    return np.mean(magnetizations)