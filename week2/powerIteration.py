# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 18:58:18 2020

Write an iterative function iterPower(base, exp) that calculates the exponential 
baseexp by simply using successive multiplication
@author: MarcoSilva
"""


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    total = 1
    
    if exp == 0:
        return 1
    
    while exp > 0:
        total *= base
        exp -= 1
        
    return total
    
print(iterPower(2.92, 8))