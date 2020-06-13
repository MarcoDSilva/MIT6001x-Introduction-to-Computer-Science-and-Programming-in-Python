# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 20:14:22 2020

@author: MarcoSilva
"""

    def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


