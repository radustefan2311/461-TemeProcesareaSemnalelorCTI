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

series_b =  trend + season + variations

trend = trend * 1e-5
season = season * 1e12

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
# autocorr = np.correlate(series_b, series_b, mode='full')
# autocorr = autocorr[autocorr.size // 2:]

# plt.title('Vectorul de autocorelație')
# plt.grid()
# plt.plot(X, autocorr, 'black')

#c
p = 50
model = AutoReg(series_b, lags=p)
model_fit = model.fit()

prediction_size = 1000 
prediction = model_fit.predict(start=N, end=N + prediction_size - 1, dynamic=False)

plt.title('Serie de timp + predictie model(rosu)')
plt.plot(X, series_b, 'black', label='Seria de timp')
plt.plot(np.arange(N, N + prediction_size), prediction, 'red', label='Model AR')
plt.plot(X, series_b, 'black')

plt.legend()
plt.tight_layout()
plt.show()