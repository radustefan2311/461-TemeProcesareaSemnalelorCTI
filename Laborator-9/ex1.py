# Codreanu Radu Stefan
# Grupa 461

import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg

# Exercitiul 1
# a

N = 1000
X = np.arange(N)

trend = 3 * X ** 2 + 3 * X - 1
season = np.cos(4 * np.pi * X) + np.sin(2 * np.pi * 3 * X)
variations = np.random.rand(N)

# trend = trend * 1e-5
# season = season * 1e12

series = trend + season + variations

# _, axs = plt.subplots(4, figsize=(12, 6))
# plt.suptitle('Serie de timp cu trei componente')

# axs[0].plot(X, series)
# axs[0].set_title('Serie de timp')
# axs[0].grid()

# axs[1].plot(X, trend)
# axs[1].set_title('Trend')
# axs[1].grid()

# axs[2].plot(X, season)
# axs[2].set_title('Sezon')
# axs[2].grid()

# axs[3].plot(X, variations)
# axs[3].set_title('Variatii mici')
# axs[3].grid()

#b

alf = 0.95
size = len(series)
arr = np.zeros(size)

for t in range(size):
    s = 0
    for i in range(1, t + 1):
        s = s + ((1 - alf) ** (t-i)) * series[i]
    arr[t] = alf * s + ((1 - alf) ** t) * series[0]


plt.plot(X, arr, label="Mediere", color = 'red')
plt.plot(X, series, label="Serie originala", color = 'black')

plt.tight_layout()
plt.legend()
plt.show()
