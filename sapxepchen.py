# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 20:27:13 2020

@author: pc
"""

x=[11,5,3,2,49,56,32,45]
for i in range(len(x)-1):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            x[i],x[j]=x[j],x[i]
            #print(x)
print(x)    