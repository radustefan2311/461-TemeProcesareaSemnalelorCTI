# Codreanu Radu Stefan
# Grupa 461

import numpy as np
import matplotlib.pyplot as plt

# Exercitiul 6

t = np.linspace (0, 4, 200)
f = 85

f0_a = f/2
f0_b = f/4
f0_c = 0

s_x1 = np.sin(2 * np.pi * f0_a * t)
s_x2 = np.sin(2 * np.pi * f0_b * t)
s_x3 = np.sin(2 * np.pi * f0_c * t)

fig, axs = plt.subplots(3)
fig.suptitle('Exercitiul 6')
axs[0].plot(t, s_x1)
axs[0].set_title('s_x1')
axs[0].set_xlabel('Timp')
axs[0].set_ylabel('Magnitudine')
axs[1].plot(t,s_x2)
axs[1].set_title('s_x2')
axs[1].set_xlabel('Timp')
axs[1].set_ylabel('Magnitudine')
axs[2].plot(t,s_x3)
axs[2].set_title('s_x3')
axs[2].set_xlabel('Timp')
axs[2].set_ylabel('Magnitudine')

plt.tight_layout()
plt.show()

# Cu cat freceventele fundamentale scad cu atat semnalul oscileaza mai putin pana ajunge la punctul 0, acesta indicand o valoare constanta a sinusoidei.