# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 16:25:47 2020

First, write a procedure, called how_many, which returns the sum of the 
number of values associated with a dictionary

@author: MarcoSilva
"""


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    total = 0
    for n in aDict:
        for k in aDict[n]:
            total += 1
            
    return total
