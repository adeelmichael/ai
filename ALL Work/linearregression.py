# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 19:12:01 2018

@author: Adeel Michael
"""


def linear_regression(X,y,m_current=0,b_current=0,epocs=1000,lr=0.0001):
    N = float(len(y))
    for i in range(epocs):
        y_current = (m_current*X) + b_current
        #erro mse
        cost = sum([data**2 for data in (y-y_current)])/N
        if i % 100 == 0:
            print(cost)
        #m_gradient
        m_gradient = -(2/N) * sum(X*(y-y_current))
        #b_gradient 
        b_gradient = -(2/N) * sum(y-y_current)
        #update m and b
        m_current = m_current - (lr*m_gradient)
        b_current = b_current - (lr*b_gradient)
        
    return m_current, b_current, cost

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([15,13,18,20,22,18,25,30,28,25])
plt.scatter(x,y)
m,b,cost = linear_regression(x,y)
plt.plot(x,m*x+b)
plt.show()