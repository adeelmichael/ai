# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 21:03:38 2018

@author: Adeel Michael
"""

import pandas as pd

#import dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,3].values

#taking care of missing values with sklearn
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN", strategy='mean', axis=0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])
#print(X)

from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
labelencoder_Y = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0])
Y[:] = labelencoder_Y.fit_transform(Y[:])
#print(X[:,0])
#print(Y[:])

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features=[0])
onehotencoded_country = onehotencoder.fit_transform(X).toarray()
print(onehotencoded_country[:,0:3])
