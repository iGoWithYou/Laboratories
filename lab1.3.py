# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 17:12:27 2019

@author: Mati
"""
y=[7,3,4,6,5]
def findLowestValue(array):
    value = min(array)
    valueIndex = array.index(value)
    return valueIndex, value
    
findLowestValue(y)
