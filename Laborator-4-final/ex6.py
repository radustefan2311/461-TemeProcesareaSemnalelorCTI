# Codreanu Radu Stefan
# Grupa 461

import numpy as np
from scipy.io import wavfile

# Exercitiul 6

#a
signal = wavfile.read('ex5.wav')

#b
group = int(0.01 * 44100)
overlap = group // 2
