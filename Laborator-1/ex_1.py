import numpy as np
import matplotlib.pyplot as plt

#Exercitii Laborator 1 - EX 1

t = np.arange(0, 0.03, 0.0005)

x_t = np.cos(520 * np.pi * t + np.pi/3)
y_t = np.cos(280 * np.pi * t - np.pi/3)
z_t = np.cos(120 * np.pi * t + np.pi/3)

#a
"""
plt.figure(figsize=(10, 6))
plt.plot(t, x_t, label='x(t)')
plt.plot(t, y_t, label='y(t)')
plt.plot(t, z_t, label='z(t)')
plt.xlabel('Timp')
plt.ylabel('Magnitudine')
plt.title('Simulare axa reala de timp')
plt.legend(loc='upper left')
plt.show()
"""


# b
"""
fig, axs = plt.subplots(3)
fig.suptitle('Construire semnale - sub. b')

axs[0].plot(t, x_t)
axs[0].set_title('Semnal x(t)')
axs[0].set_xlabel('Timp')
axs[0].set_ylabel('Magnitudine')


axs[1].plot(t, y_t)
axs[1].set_title('Semnal y(t)')
axs[1].set_xlabel('Timp')
axs[1].set_ylabel('Magnitudine')


axs[2].plot(t, z_t)
axs[2].set_title('Semnal z(t)')
axs[2].set_xlabel('Timp')
axs[2].set_ylabel('Magnitudine')

plt.tight_layout()
plt.show()
"""
# c
"""
f = 200  
t_new = np.arange(0, 0.03, 1 / f)

x_n = np.cos(520 * np.pi * t_new + np.pi/3)
y_n = np.cos(280 * np.pi * t_new - np.pi/3)
z_n = np.cos(120 * np.pi * t_new + np.pi/3)

fig, axs = plt.subplots(3)
fig.suptitle('Construire semnale - sub. c')

axs[0].stem(t_new, x_n)
axs[0].plot(t, x_t)
axs[0].set_title('x[n] eșantionat')
axs[0].set_xlabel('Timp')
axs[0].set_ylabel('Magnitudine')

axs[1].stem(t_new, y_n)
axs[1].plot(t, y_t)
axs[1].set_title('y[n] eșantionat')
axs[1].set_xlabel('Timp')
axs[1].set_ylabel('Magnitudine')

axs[2].stem(t_new, z_n)
axs[2].plot(t, z_t)
axs[2].set_title('z[n] eșantionat')
axs[2].set_xlabel('Timp')
axs[2].set_ylabel('Magnitudine')

plt.tight_layout()
plt.show()
"""
