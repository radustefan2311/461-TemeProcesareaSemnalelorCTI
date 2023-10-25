# Codreanu Radu Stefan
# Grupa 461

import numpy as np
import matplotlib.pyplot as plt

# Exercitiul 2

t = np.linspace(0, 2, 450)

f0 = 0.85 
faza_1 = np.pi / 2
faza_2 = np.pi / 4
faza_3 = np.pi / 6
faza_4 = np.pi / 8

z = np.random.normal(0, 1, len(t))

x_1 = np.sin(2 * np.pi * f0 * t + faza_1)
x_2 = np.sin(2 * np.pi * f0 * t + faza_2)
x_3 = np.sin(2 * np.pi * f0 * t + faza_3)
x_4 = np.sin(2 * np.pi * f0 * t + faza_4)

plt.figure(figsize=(10, 6))

SNR = [0.1, 1, 10, 100]
for k in SNR:
  g = np.sqrt(np.linalg.norm(x_1) ** 2/ (k * np.linalg.norm(z) ** 2))
  plt.plot(t, x_1 + g * z)

plt.xlabel('Timp')
plt.ylabel('Magnitudine')
plt.title('Exercitiul 2 - Semnal Zgomot')
plt.legend(loc='upper left')
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(t, x_1, label='x_1')
plt.plot(t, x_2, label='x_2')
plt.plot(t, x_3, label='x_3')
plt.plot(t, x_4, label='x_4')
plt.xlabel('Timp')
plt.ylabel('Magnitudine')
plt.title('Exercitiul 2 - 4 Semnale')
plt.legend(loc='upper left')
plt.grid()
plt.show()
