# Codreanu Radu Stefan
# Grupa 461

import numpy as np
import matplotlib.pyplot as plt

# Exercitiul 4

x = np.genfromtxt('Train.csv', delimiter=',', skip_header = 1)

# a
index = np.where(x[:, 0] == 100)[0][0]

trei_zile = x[index:index + 72]

coloane = trei_zile[:, 2]

X = np.fft.fft(coloane)

t_a = np.arange(0, len(coloane))

plt.figure(figsize=(10, 6))
plt.plot(t_a, abs(X)) 
plt.xlabel('Esantioane')
plt.ylabel('Masini')
plt.title('Exercitiul 4 a.')
plt.grid()
plt.show()

# b
ω_array = [5, 9, 13, 17]

plt.figure(figsize=(10, 6))

for ω in ω_array:
    filter = np.convolve(X, np.ones(ω), 'valid') / ω
    t_b = np.arange(0, len(filter))
    plt.plot(t_b, abs(filter), label=f'Dimensiuni fereastra {ω}')

plt.xlabel('Esantioane')
plt.ylabel('Masini')
plt.title('Exercitiul 4 b.')
plt.legend()
plt.grid()
plt.show()