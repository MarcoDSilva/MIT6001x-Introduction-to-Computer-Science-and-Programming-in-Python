# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:24:54 2020

bug testing/fixing exercises

Your task is to modify the code for integerDivision
so that this error (var count referenced before assignment)
does not occur. 

@author: MarcoSilva
"""


def integerDivision(x, a):
    '''
    Parameters
    ----------
    x : int
        non negative integer argument.
    a : int
        positive integer argument.

    Returns: integer, the division of x by a
    -------
    '''
    count = 0
    
    while x >= a:
        count += 1
        x = x - 1
    return count