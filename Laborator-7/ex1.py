# Codreanu Radu Stefan
# Grupa 461

from scipy import misc, ndimage
import numpy as np
import matplotlib.pyplot as plt

# X = misc.face(gray=True)
# plt.imshow(X, cmap=plt.cm.gray)
# plt.show()

# Exercitiul 1
# a

n1=25
n2=35

xA = np.zeros((n1,n2))
for i in range(n1):
    for j in range(n2):
        xA[i,j] = np.sin(2 * np.pi * i + 3 * np.pi * j)

plt.imshow(xA, cmap=plt.cm.gray)
plt.show()

Y = np.fft.fft2(xA)
freq_db = 20*np.log10(abs(Y))

plt.imshow(freq_db)
plt.colorbar()
plt.show()

# b

xB = np.zeros((n1,n2))
for i in range(n1):
    for j in range(n2):
        xB[i,j] = np.sin(4 * np.pi * i) + np.cos(6 * np.pi * j)

plt.imshow(xB, cmap=plt.cm.gray)
plt.show()

Y = np.fft.fft2(xB)
freq_db = 20*np.log10(abs(Y))

plt.imshow(freq_db)
plt.colorbar()
plt.show()

#c

yC = np.zeros((n1, n2))
yC[0][5] = 1
yC[0][n1 - 5] = 1
 
freq_dbC = 20 * np.log10(abs(yC))
 
plt.imshow(freq_dbC)
plt.colorbar()
plt.show()
 
xC = np.fft.ifft2(yC)
 
plt.imshow(xC.real)
plt.show()
 
# d

yD = np.zeros((n1, n2))
yD[5][0] = 1
yD[n1 - 5][0] = 1
 
freq_dbD = 20 * np.log10(abs(yD))
 
plt.imshow(freq_dbD)
plt.colorbar()
plt.show()
 
x_D = np.fft.ifft2(yD)
 
plt.imshow(x_D.real)
plt.show()

# e

yE = np.zeros((n1, n2))
yE[5][5] = 1
yE[n1 - 5][n2 - 5] = 1
 
freq_dbE = 20 * np.log10(abs(yE))
 
plt.imshow(freq_dbE)
plt.colorbar()
plt.show()
 
xE = np.fft.ifft2(yE)
 
plt.imshow(xE.real)
plt.show()