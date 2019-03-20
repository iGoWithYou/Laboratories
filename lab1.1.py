# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:01:09 2019

@author: Mati
"""
from math import*
x = 56
z = 0
while x <= 100:
    y = 2*(x**2) + 2*x + 2
    print('for x = ',x,'function value y = ',y)
    x = x+1;
    z = z + y;
print('function y total value = ',z)