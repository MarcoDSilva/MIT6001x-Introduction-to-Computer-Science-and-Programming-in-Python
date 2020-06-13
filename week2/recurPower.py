# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 18:34:16 2020

Write a function recurPower(base, exp) which computes baseexp by recursively 
calling itself to solve a smaller version of the same problem, and then 
multiplying the result by base to solve the initial problem. 

@author: MarcoSilva
"""


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    else:
        return base * recurPower(base,exp - 1)
    
print (recurPower(-6.66,4))