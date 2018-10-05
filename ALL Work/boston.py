# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 20:32:35 2018

@author: Adeel Michael
"""
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

boston = load_boston()
#boston data is a dictionary data type
#print(boston.keys())
#print(boston.data.shape)
#print(boston.target.shape)
#print(boston.feature_names)
#print(boston.DESCR)

bos = pd.DataFrame(boston.data)
#print(bos.head())
bos.columns = boston.feature_names
#print(bos.head())
bos['price'] = boston.target
#print(bos.head())
#print(bos.describe())
##########################
#all columns accept price
x = bos.drop('price', axis=1)
#only price
y = bos['price']
#test size is 20% i.e 0.2
#80 or 0.8 will be for training
X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.2,random_state=10)
lr = LinearRegression()
lr.fit(X_train, Y_train)
Y_pred = lr.predict(X_test)

plt.scatter(Y_test, Y_pred)




