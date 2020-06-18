# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:09:31 2020

Write a procedure called oddTuples, which takes a tuple as input,
 and returns a new tuple as output, where every other element 
 of the input tuple is copied, starting with the first one.
 
@author: MarcoSilva
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    odd = ()
    
    for x in range(0,len(aTup)):
        if x % 2 == 0:
            odd = odd + (aTup[x],)
    
    return odd
            
        



