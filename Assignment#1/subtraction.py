# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 17:45:35 2018

@author: Adeel Michael
"""

a = [[1,2,3]]
b = [[7,8,3]]
result = [[0, 0, 0]]

for i in range(len(a)):
    for j in range(len(a[i])):   
        result[i][j] = a[i][j] - b[i][j]   
        
for r in result:
    print(r)   
