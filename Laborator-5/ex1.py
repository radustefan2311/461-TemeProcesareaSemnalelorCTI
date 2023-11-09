# Codreanu Radu Stefan
# Grupa 461

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Exercitiul 1

#a

#In laboratorul de astazi veti lucra cu un semnal real. Numarul de masini care trec printr-o intersectie a fost masurat din ora in ora. --> Informatie preluata din laboratorul 5

# Deci avem timpul de esantionare, ts = 3600 sec
# Din lab 2 aflam ca frecventa de esantionare se defineste fs = 1/ts.
# fs ≈ 0.000277778

df = pd.read_csv('Train.csv')
# plt.figure(figsize=(10, 6))
# plt.plot(df['ID'], df['Count'])
# plt.title('Exercitiul 1')
# plt.xlabel('Esantioane')
# plt.ylabel('Nr masini')
# plt.grid(True)
# plt.show()


#b

# Avem 18288 eșantioane
# Deci 18288/ora, 18288 de ore

#c

#Teorema se aplica pentru semnale limitate ın banda si stabileste o relatie intre frecventa minima de esantionare, fs si frecventa maxima continuta in semnal, B, anume: pentru a nu avea pierderi de informatie, un semnal trebuie esantionat cu fs > 2B. --> Laborator 4

# 0.000277778 > 2B => B < 0.000138889 

#d

X = np.fft.fft(df['Count'])

half_index = len(df) // 2
df_first_half = df.iloc[:half_index]
X_first_half = X[:half_index]

plt.figure(figsize=(10, 6))
plt.plot(df_first_half['ID'], np.abs(X_first_half))
plt.title('FFT Plot - First Half of ID vs. X')
plt.xlabel('ID')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
