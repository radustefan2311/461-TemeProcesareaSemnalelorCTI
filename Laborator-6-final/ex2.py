# Codreanu Radu Stefan
# Grupa 461

import numpy as np
import matplotlib.pyplot as plt

# Exercitiul 2

N = 5 
p = np.random.randint(-5, 5, N + 1)
q = np.random.randint(-5, 5, N + 1)

r_direct = np.convolve(p, q)

print("Inmultire directa polinoame p * q")
print(r_direct)

fft_p_q = np.fft.fft(p, n=2*N+1) * np.fft.fft(q, n=2*N+1)
r_fft = np.real(np.fft.ifft(fft_p_q ))

print("Inmultire fft polinoame p * q")
print(r_fft)