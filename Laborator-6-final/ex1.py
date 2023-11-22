# Codreanu Radu Stefan
# Grupa 461

import numpy as np
import matplotlib.pyplot as plt

# Exercitiul 1

N = 100
x = np.random.rand(N)

fig, axs = plt.subplots(4)

axs[0].plot(x)
axs[0].grid()
plt.title('Grafic Initial')

x = np.convolve(x,x)
axs[1].plot(x)
axs[1].grid()
plt.title('Iteratia 1: x ← x * x')

x = np.convolve(x,x)
axs[2].plot(x)
axs[2].grid()
plt.title('Iteratia 2: x ← x * x')

x = np.convolve(x,x)
axs[3].plot(x)
axs[3].grid()
plt.title('Iteratia 3: x ← x * x')

plt.tight_layout()
plt.show()