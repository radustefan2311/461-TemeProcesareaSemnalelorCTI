# Codreanu Radu Stefan
# Grupa 461

import numpy as np
import matplotlib.pyplot as plt

# Exercitiul 4

f0_c = 240 
t_saw = np.linspace(0, 0.08, 750) 
sawtooth = 2* (t_saw * 240 - np.floor(1 / 2 + t_saw * 240))

f0_a = 400
t_sin = np.linspace(0, 0.08, 750)
sinusoidal = np.sin(2 * np.pi * f0_a * t_sin)

suma = sawtooth + sinusoidal

fig, axs = plt.subplots(3)
fig.suptitle('Exercitiul 4')
axs[0].stem(t_saw,sawtooth)
axs[0].set_title('Semnal Sawtooth')
axs[0].set_xlabel('Timp')
axs[0].set_ylabel('Magnitudine')
axs[1].stem(t_sin, sinusoidal)
axs[1].set_title('Semnal Sinusoidal')
axs[1].set_xlabel('Timp')
axs[1].set_ylabel('Magnitudine')
axs[2].stem(t_sin,suma)
axs[2].set_title('Suma Semnale')
axs[2].set_xlabel('Timp')
axs[2].set_ylabel('Magnitudine')

plt.tight_layout()
plt.show()