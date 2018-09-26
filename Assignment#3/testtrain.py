# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 15:44:27 2018

@author: Adeel Michael
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

TrainData = pd.read_csv('train.csv');

labels = TrainData.iloc[:,0].values
features = TrainData.iloc[:,1].values

X_train,X_test,Y_train,Y_test = train_test_split(labels,features,test_size=0.2,random_state=10)
lr = LinearRegression()
lr.fit(X_train, Y_train)
Y_pred = lr.predict(X_test)

plt.scatter(Y_test, Y_pred)
