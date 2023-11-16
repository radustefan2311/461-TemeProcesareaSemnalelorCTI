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

# In laboratorul de astazi veti lucra cu un semnal real. Numarul de masini care
# trec printr-o intersectie a fost masurat din ora in ora. In referinta de mai
# sus, fisierul Train.csv1 contine 18288 esantioane din acest semnal.
# Avem 18288 eșantioane
# Deci 18288/ora, 18288 de ore

#c

#Teorema se aplica pentru semnale limitate ın banda si stabileste o relatie intre frecventa minima de esantionare,
# fs si frecventa maxima continuta in semnal, B, anume: pentru a nu avea pierderi de informatie, un semnal trebuie esantionat cu fs > 2B. --> Laborator 4

# 0.000277778 > 2B => B < 0.000138889 

#d

# X = np.fft.fft(df['Count'])

# half_index = len(df) // 2
# df_first_half = df.iloc[:half_index]
# X_first_half = X[:half_index]

# plt.figure(figsize=(10, 6))
# plt.plot(df_first_half['ID'], np.abs(X_first_half))
# plt.title('FFT Plot - Prima jumatate ID vs. X')
# plt.xlabel('ID')
# plt.ylabel('Transformata')
# plt.grid(True)
# plt.show()

#g

# df = pd.read_csv('Train.csv')
# esantion_g = np.where(df.iloc[:, 0].values == 3420)[0][0]
# month = df.iloc[esantion_g:esantion_g + 744, :]
# X = np.fft.fft(month['Count'])
# T = np.arange(0, len(month['Count']))
# plt.figure(figsize=(10, 6))
# plt.plot(T, np.abs(X))
# plt.title('Subpunct G')
# plt.xlabel('Timp')
# plt.ylabel('|X|')
# plt.yscale("log")
# plt.grid(True)
# plt.show()

#i

collumns = df.iloc[:, 0]
query_collumns = collumns[collumns < 1065]

X = np.fft.fft(query_collumns)
T = np.arange(0, len(query_collumns))

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(T, np.abs(X))
plt.title('FFT pentru date filtrate')
plt.xlabel('Timp')
plt.ylabel('|X|')
# plt.yscale("log")
plt.grid(True)
plt.show()

# Am observat ca incepand de la esantionul 1065, numarul de masini incepe sa creasca semnificativ