# Codreanu Radu Stefan
# Grupa 461

import numpy as np
import matplotlib.pyplot as plt

# Exercitiul 3

N = 1450
T = np.linspace(0, 2, N)

ω = [10, 25, 80]
x = np.cos(2 * np.pi * ω[0] * T) + 2.5 * np.cos(2 * np.pi * ω[1] * T) + 1.5 * np.sin(2 * np.pi * ω[2] * T)

X = np.empty(N, dtype=complex)
for m in range(N):
    for n in range(N):
        X[m] += x[n] * np.exp(-2 * np.pi * 1j * n * m / N)

_, axs = plt.subplots(2)
axs[0].plot(T, x)
axs[0].set_xlabel('Timp(s)')
axs[0].set_ylabel('x(t)')
axs[0].grid()

axs[1].stem(np.arange(N), np.sqrt(X.real**2 + X.imag**2), linefmt='black', basefmt=' ')
axs[1].set_xlabel('Frecvența (Hz)')
axs[1].set_ylabel('|X(ω)|')
axs[1].grid()

plt.show()