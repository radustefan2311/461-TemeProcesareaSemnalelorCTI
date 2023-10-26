# Codreanu Radu Stefan
# Grupa 461

from cmath import exp
import numpy as np
import matplotlib.pyplot as plt

# Exercitiul 1

import numpy as np
import matplotlib.pyplot as plt

N = 8
T = np.linspace(0, 0.5, N)
X = np.sin(2 * np.pi * T)
F = np.zeros((N, N), dtype=complex)

for m in range(N):
    for n in range(N):
        F[m][n] = np.exp(2 * np.pi * 1j * m * n / N)

F = np.dot(F, X)

_, axs = plt.subplots(N, 2)
plt.suptitle('Partea reala-imaginara a elementelor din matricea Fourier')

for i in range(N):
    axs[i][0].plot(np.arange(N), F.real, 'b')  
    axs[i][1].plot(np.arange(N), F.imag, 'r')  

check = np.allclose(np.dot(F, F.conj().T), np.eye(N))

if check:
    print("Matricea Fourier este complexa si ortogonala")
else:
    print("Matricea Fourier nu este complexa si ortogonala")

plt.show()