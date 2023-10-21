import numpy as np
import matplotlib.pyplot as plt

#Exercitii Laborator 1 - EX 2

#a
"""
f0 = 400
t = np.linspace(0, 0.02 , 1600)
s_a = np.sin(2 * np.pi * f0 * t)

fig, axs = plt.subplots(1)
fig.suptitle('Construire semnale')

axs.stem(t, s_a)
axs.set_title('Semnal sinusoidal s_a')
axs.set_xlabel('Timp')
axs.set_ylabel('Magnitudine')
"""

#b 
"""
f0 = 800
t = np.linspace(0, 3 , 1100)
s_b = np.sin(2 * np.pi * f0 * t)

fig, axs = plt.subplots(1)
fig.suptitle('Construire semnale')

axs.plot(t, s_b)
axs.set_title('Semnal sinusoidal s_b')
axs.set_xlabel('Timp')
axs.set_ylabel('Magnitudine')
"""

#c 
"""
f = 240
t = np.linspace(0, 0.08, 750)
s_c = 2*(t * 240 - np.floor(1 / 2 + t * 240))

fig, axs = plt.subplots(1)
fig.suptitle('Construire semnale')

axs.plot(t, s_c)
axs.set_title('Semnal sawtooth s_c')
axs.set_xlabel('Timp')
axs.set_ylabel('Magnitudine')
"""

#d
"""
f = 300
t = np.linspace(0, 0.08, 750)
s_d = np.sign(np.sin(2 * np.pi * f * t))

fig, axs = plt.subplots(1)
fig.suptitle('Construire semnale')

axs.plot(t, s_d)
axs.set_title('Semnal square s_d')
axs.set_xlabel('Timp')
axs.set_ylabel('Magnitudine')
"""

#e
"""
s_e = np.random.rand(128, 128)

fig, axs = plt.subplots(1)
fig.suptitle('Construire semnale')

axs.imshow(s_e, cmap='inferno')
axs.set_title('Semnal 2D aleator s_e')
axs.set_xlabel('Timp')
axs.set_ylabel('Magnitudine')
"""
#f
"""
s_f = np.ones((128, 128))
s_f = [[(i + j) * (i - j) for j in range(128)] for i in range(128)]

fig, axs = plt.subplots(1)
fig.suptitle('Construire semnale')

axs.imshow(s_f, cmap='inferno')
axs.set_title('Semnal 2D s_f')
axs.set_xlabel('Timp')
axs.set_ylabel('Magnitudine')
"""
plt.tight_layout()
plt.show()
