# Codreanu Radu Stefan
# Grupa 461

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt

# Exercitiul 3

X = misc.face(gray=True)

Y = np.fft.fft2(X)
freq_db = 20 * np.log10(abs(Y))

pixel_noise = 250
noise = np.random.randint(-pixel_noise, high=pixel_noise + 1, size=X.shape)
X_noisy = X + noise

plt.imshow(X, cmap=plt.cm.gray)
plt.title('raportul SNR înainte')
plt.show()
plt.imshow(X_noisy, cmap=plt.cm.gray)
plt.title('raportul SNR dupa')
plt.show()