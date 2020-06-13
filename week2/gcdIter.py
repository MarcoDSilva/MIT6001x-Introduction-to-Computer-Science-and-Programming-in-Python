# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 19:59:40 2020

The greatest common divisor of two positive integers is the largest integer 
that divides each of them without remainder.

@author: MarcoSilva
"""

def gcdIter(a,b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    smaller_num = 0
    common_divisor = 1
    i = 1
     
    if a > b:
        smaller_num = b
    else:
        smaller_num = a
         

    while i <= smaller_num:
        if a % i == 0 and b % i == 0:
            common_divisor = i
        
        i += 1
    
    return common_divisor


print(gcdIter(2,12))