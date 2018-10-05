# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 18:36:57 2018

@author: Adeel Michael
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('Social_Network_Ads.csv')

x = data.iloc[:,2:4].values
y = data.iloc[:,-1].values

X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.2,random_state=10)

sc = SVC(C=1.0, kernel='linear')

sc.fit(X_train, Y_train)

y_pred = sc.predict(X_test)


# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, Y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                    np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, sc.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
            alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
   plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
               c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('SVM (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()