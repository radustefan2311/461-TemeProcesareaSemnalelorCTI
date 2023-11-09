# Codreanu Radu Stefan
# Grupa 461

import time
import numpy as np
import matplotlib.pyplot as plt

# Exercitiul 2

t = np.linspace(0, 1, 2000)
t_es = np.linspace(0, 1, 9)
fig, axs = plt.subplots(4)
axs[0].plot(t, np.sin(2 * np.pi * 18 * t), c="magenta")

axs[1].plot(t, np.sin(2 * np.pi * 18 * t), c="magenta")
axs[1].scatter(t_es, np.sin(2 * np.pi * 18 * t_es), c="yellow")

axs[2].plot(t, np.sin(2 * np.pi * 10 * t), c="purple")
axs[2].scatter(t_es, np.sin(2 * np.pi * 10 * t_es), c="yellow")

axs[3].plot(t, np.sin(2 * np.pi * 6 * t), c="green")
axs[3].scatter(t_es, np.sin(2 * np.pi * 6 * t_es), c="yellow")

plt.tight_layout()
plt.show()

#Not working properly
