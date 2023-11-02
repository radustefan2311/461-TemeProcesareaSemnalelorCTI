# Codreanu Radu Stefan
# Grupa 461

import numpy as np
import matplotlib.pyplot as plt

# Exercitiul 1

N = 8
T = np.linspace(0, 3, N)
F = np.zeros((N, N), dtype=complex)

for m in range(N):
    for n in range(N):
        F[m][n] = np.exp(2 * np.pi * 1j * m * n / N)

_, axs = plt.subplots(N, 2)
plt.suptitle('Partea reala-imaginara a elementelor din matricea Fourier')

for i in range(N):
    axs[i, 0].plot(np.arange(N), F[i].real, 'g')
    axs[i, 1].plot(np.arange(N), F[i].imag, 'y')

check = np.allclose(np.dot(F, F.conj().T), np.eye(N))

if check:
    print("Matricea Fourier este complexa si ortogonala")
else:
    print("Matricea Fourier nu este complexa si ortogonala")

plt.show()
