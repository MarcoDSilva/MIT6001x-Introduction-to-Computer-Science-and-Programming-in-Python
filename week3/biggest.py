# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:40:33 2020

This time, write a procedure, called biggest, which returns the key 
corresponding to the entry with the largest number of values associated with it. 
If there is more than one such entry, return any one of the matching keys.

@author: MarcoSilva
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    longest = max((aDict.values()))
    long = len(longest)
    
    values = []
    
    for k in aDict:
        if len(aDict[k]) == long:
            values.append(k)
            
    if len(values) == 0:
        return None
    elif len(values) == 1:
        return values[0]
    else:           
        return values
        