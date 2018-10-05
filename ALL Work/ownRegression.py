# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 15:19:06 2018

@author: Adeel Michael
"""


def custom_regression(X,y,m_current=0,b_current=0,epocs=1000,lr=0.0001):
    N = float(len(y))
    for i in range(epocs):
        y_current = (m_current*X) + b_current
    
        cost = sum([res**2 for res in (y-y_current)])/N
        if i % 100 == 0:
            print(cost)
        
        m_gradient = -2/N * sum(X*(y-y_current))
        
        b_gradient = -2/N * sum(y-y_current)
        
        m_current = m_current - (lr*m_gradient)
        b_current = b_current - (lr*b_gradient)
        
    return m_current, b_current, cost

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('train.csv')
x = data.iloc[:,0].values
y = data.iloc[:,1].values

plt.scatter(x,y)

m,b,cost = custom_regression(x,y)
plt.plot(x,m*x+b)
plt.show()
