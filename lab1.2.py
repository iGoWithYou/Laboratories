# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:52:55 2019

@author: Mati
"""

n=int(input("podaj liczbe"))

fact = 1;
for i in range(1,n+1):
    fact = fact * i
print('factorial of your number:',n,'has value: ',fact)