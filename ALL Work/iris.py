# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:56:37 2018

@author: Adeel Michael
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

data = pd.read_csv('iris.csv')

x = data.iloc[:,1:4].values
y = data.iloc[:,-1].values



X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.2,random_state=0)
lr = LogisticRegression()

lr.fit(X_train,Y_train)
y_pred = lr.predict(X_test)
#print(y_pred.size)
plt.scatter(Y_test,y_pred)
plt.show()