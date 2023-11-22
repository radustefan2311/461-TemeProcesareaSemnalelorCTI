# Codreanu Radu Stefan
# Grupa 461

import numpy as np
import matplotlib.pyplot as plt

# Exercitiul 3

def Dreptunghiulara(X):
    w = np.ones(len(X))
    return w

def Hanning(X):
    w = 0.5 * (1 - np.cos(2* np.pi * X/len(X)))
    return w

Nω = 200
fs = 100
t = np.linspace(0, 1, Nω)
x = np.sin(2 * np.pi * fs * t)

plt.figure(figsize=(10, 6))
plt.plot(t, Dreptunghiulara(x) * x, label='Dreptunghiulara')
plt.plot(t, Hanning(x) * x, label='Hanning')
plt.title('Exercitiul 3')
plt.legend() 
plt.show()