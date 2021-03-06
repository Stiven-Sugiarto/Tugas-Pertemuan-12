# -*- coding: utf-8 -*-
"""Regresi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ht9q2tEZ1KEzkMwNELbLPSuSRpApx8op
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

dataset = pd.read_excel('datamobil.xlsx')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

dataset.keys()

dataset.shape

dataku = pd.DataFrame(dataset)
dataku.head()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)



y_pred = regressor.predict(x_test)

plt.scatter(dataku.Usia Mobil , dataku.Harga Mobil)
plt.xlabel("Usia Mobil")
plt.ylabel("Harga Mobil")
plt.title("Grafik Usia Mobil vs Harga Mobil")
plt.show

plt.figure(figsize=(10,8))
plt.scatter(x_train, y_train, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')
plt.title('Usia Mobil terhadap Harga Mobil(Training set')
plt.xlabel('Usia Mobil')
plt.ylabel('Harga Mobil')
plt.show