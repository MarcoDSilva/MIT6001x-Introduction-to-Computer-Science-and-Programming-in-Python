# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 18:30:18 2020

@author: MarcoSilva
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    def f(x):
        total = 0
        fact = len(L) - 1 
        
        for num in L:
            print(num)
            total += num * x**fact
            fact -= 1
        
        return total
    
    return f
