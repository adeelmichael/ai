# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 17:46:19 2018

@author: Adeel Michael
"""

a = [[1,2,3], [1,5,6]]
b = [[7,8,3], [2,4,3]]
result = [[0, 0, 0],[0,0,0]]

 

 
#Addition of the above matrices by function 
def addition(a, b):
       for i in range(len(a)):
           for j in range(len(a[i])):   
               result[i][j] = a[i][j] + b[i][j]   
       for r in result:
           print(r)
       
addition(a, b)
        
#subtraction function 
def subtration(a, b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            result[i][j] = a[i][j] - b[i][j]
    for r in result:
        print(r)

subtration(a, b)        

#multiplication
def multiplication(a, b):
    for i in range(len(a)):
        for j in range(len(b[i])):
            result[i][j] = a[i][j] * b[i][j]
    for r in result:
        print(r)
        
multiplication(a,b)
        