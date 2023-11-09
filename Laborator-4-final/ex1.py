# Codreanu Radu Stefan
# Grupa 461

import time
import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter

# Exercitiul 1

N = [128, 256, 512, 1024, 2048, 4096, 8192]
fourier_manual = []
fourier_fft = []


for step in N:
    
  t = np.linspace(0, 1, step)
  x = np.sin(2 * np.pi * t)
  Fourier_manual = np.zeros((step, step), dtype=complex)
  # Manual Fourier implementation
  start_manual = time.time()
  for m in range(step):
      for n in range(step):
          Fourier_manual[m][n] = np.exp(2 * np.pi * 1j * m * n / step)

  X = np.dot(Fourier_manual, x)
  end_manual = time.time()
  fourier_manual.append(end_manual - start_manual)

  # FFT Fourier implementation
  start_fft = perf_counter()

  Fourier_fft = np.fft.fft(x)

  end_fft = perf_counter()
  fourier_fft.append(end_fft - start_fft)

plt.figure(figsize=(10,6))
plt.plot(N, fourier_manual, marker='o')
plt.plot(N, fourier_fft, marker='o')
plt.xlabel('N')
plt.ylabel('Timp')
plt.yscale('log')
plt.title('Manual vs Fft')
plt.show()

