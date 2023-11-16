# Codreanu Radu Stefan
# Grupa 461

import numpy as np
import matplotlib.pyplot as plt

# Exercitiul 2

N = 5 
p = np.random.randint(-5, 5, N + 1)
q = np.random.randint(-5, 5, N + 1)

r_direct = np.convolve(p, q)

print(r_direct)

size = 2 ** int(np.ceil(np.log2(len(p) + len(q) - 1)))
    
p_padded = np.pad(p, (0, size - len(p)), mode='constant')
q_padded = np.pad(q, (0, size - len(q)), mode='constant')

fft_p = np.fft.fft(p_padded)
fft_q = np.fft.fft(q_padded)

fft_result = fft_p * fft_q

result = np.fft.ifft(fft_result).real
result = np.round(result).astype(int)

print(result)