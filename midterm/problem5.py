# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 16:32:17 2020

Write a Python function that returns a list of keys in aDict that map to 
integer values that are unique (i.e. values appear exactly once in aDict).
The list of keys you return should be sorted in increasing order. 
(If aDict does not contain any unique values, you should return an empty list.)

@author: MarcoSilva
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''    
    d = {}
    l = []
    
    # for each key in the dictionary we check if the respective value exists in
    # the dictionary, if it does we update, otherwise we add a new one    
    for k in aDict:     
        val = aDict[k]
        
        if val in d:
            d[val] += 1
        else:
            d[val] = 1
            
    # for each value in the new dict, if it only has showed one time
    # we get the key from aDict and add it to the list to return
    for v in d:
        if d[v] == 1:
            l.append(getIndex(aDict,v))
    
    # sorting because we need to return in order
    l.sort()
    return l
    
def getIndex(aDict, val):
    '''
    Receives a dictionary and a value to search
    If any key corresponds to that value, that key is returned 
    '''
    
    for k in aDict:
        if aDict[k] == val:
            return k
    
    return None