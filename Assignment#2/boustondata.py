# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:26:38 2018

@author: Adeel Michael
"""
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
boston = load_boston()
'''
print(boston.keys())
print(boston.data.shape)
print(boston.feature_names)
print(boston.DESCR)
'''
bos = pd.DataFrame(boston.data)
#print(bos.head())

#bos.columns = boston.feature_names
#print(bos.head())

#print(bos.describe)
bos['PRICE'] = boston.target
#Y is Boston Prices
#X is all other Features

X = bos.drop('PRICE', axis=1)
Y = bos['PRICE']

#print(bos['PRICE'])

X_train, X_test, Y_train, Y_test = sklearn.cross_validation.train_test_split(X, Y, test_size = 0.33, random_state=5)
'''
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)
'''
from sklearn.linear_model import LinearRegression

lm = LinearRegression()

lm.fit(X_train, Y_train)

Y_pred = lm.predict(X_test)

plt.scatter(Y_test, Y_pred)
plt.xlabel("Prices: $Y_i$")
plt.ylabel("Predicted prices: $\hat{Y}_i$")
plt.title("Prices vs Predicted prices: $Y_i$ vs $\hat{Y}_i$")

mse = sklearn.metrics.mean_squared_error(Y_test, Y_pred)
print(mse)