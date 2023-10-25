# Codreanu Radu Stefan
# Grupa 461

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as snd
import scipy

# Exercitiul 3
#a
f0_a = 400
t_a = np.linspace(0, 0.02, 1600)
s_a = np.sin(2 * np.pi* f0_a * t_a)

#b
f0_b = 800 
t_b = np.linspace(0, 3, 1100)
s_b = np.sin(2* np.pi * f0_b *t_b)

#c
f0_c = 240 
t_c = np.linspace(0, 0.08, 750) 
s_c = 2* (t_c * 240 - np.floor(1 / 2 + t_c * 240))

#d
f0_d = 300 
t_d = np.linspace(0, 0.08, 750) 
s_d = np.sign(np.sin(2 * np.pi * f0_d * t_d))

snd.play(s_a)
snd.wait()
snd.play(s_b)
snd.wait()
snd.play(s_c)
snd.wait()
snd.play(s_d)
snd.wait()

scipy.io.wavfile.write('s_a.wav', 44100, s_a)
scipy.io.wavfile.read('s_a.wav')
