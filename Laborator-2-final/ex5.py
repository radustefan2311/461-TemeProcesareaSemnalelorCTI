# Codreanu Radu Stefan
# Grupa 461

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as snd
import time

# Exercitiul 5

f0_x= 150
f0_y = 350
t = np.linspace(0, 2, 1100)

sq_x = np.sign(np.sin(2 * np.pi * f0_x * t))
sq_y = np.sign(np.sin(2 * np.pi * f0_y * t))

concatenate = np.concatenate((sq_x, sq_y))

snd.play(sq_x, samplerate= 2000)
snd.wait()
snd.stop()

snd.play(sq_y, samplerate= 2000)
snd.wait()
snd.stop()

snd.play(concatenate, samplerate= 2000)
snd.wait()
snd.stop()

# Concatenarea reprezinta sunetul celor 2 semnale combinat