# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 18:43:50 2020

Write a function is_triangular that meets the specification below. 
A triangular number is a number obtained by the continued summation of integers starting from 1. 
For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers. 
@author: MarcoSilva
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    
    if k == 0 or k < 0:
        return False
    
    total = 0
    
    # starting from 1 and until we reach k , we sum the numbers to get the triangular ones
    # if we hit the number with this sum, we return true because we found it
    # if we don't find a result, we return false
    
    for n in range(0, k+1):
        total += n
        
        if total == k:
            return True
    
    return False
