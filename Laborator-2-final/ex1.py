# Codreanu Radu Stefan
# Grupa 461

import numpy as np
import matplotlib.pyplot as plt

# Exercitiul 1

t = np.linspace(0, 2)

f0 = 0.85 
faza = 0 

x = np.sin(2 * np.pi * f0 * t + faza)
y = np.cos(2 * np.pi * f0 * t + faza - np.pi/2 )

fig, axs = plt.subplots(2)
fig.suptitle('Exercitiul 1')

axs[0].plot(t, x)
axs[0].set_title('Sinus')
axs[0].set_xlabel('Timp')
axs[0].set_ylabel('Magnitudine')
axs[0].grid()

axs[1].plot(t, y)
axs[1].set_title('Cosinus Deplasat')
axs[1].set_xlabel('Timp')
axs[1].set_ylabel('Magnitudine')
axs[1].grid()

plt.tight_layout()
plt.show()
