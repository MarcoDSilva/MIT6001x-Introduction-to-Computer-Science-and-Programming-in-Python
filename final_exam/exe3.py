# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 21:14:14 2020

You are given a dictionary aDict that maps integer keys to integer values. 
Write a Python function that returns a list of keys in aDict that map to dictionary values that appear exactly once in aDict. 

    This function takes in a dictionary and returns a list.
    Return the list of keys in increasing order.
    If aDict does not contain any values appearing exactly once, return an empty list.
    If aDict is empty, return an empty list.


@author: MarcoSilva
"""

def get_values(dic):
    '''
        dic: dictionary of integers as keys and as values
        returns a list of values that are equal or greater than 0
    '''
    
    values = []
    for key in dic:
        if dic[key] >= 0:
            values.append(dic[key])
    
    return values

def get_single_nums(L):
    '''
        L: list of integers
        returns a list of integers that only show up once

    '''
    dic = {}
    
    # dic to get the count of the ints that show up
    for num in L:
        if dic.get(num, -1) < 0:
            dic[num] = 1
        else:
            dic[num] += 1
    
    singles = []
    
    for key in dic:
        if dic[key] == 1:
            singles.append(key)
    
    return singles

def get_keys(L, dic):
    ''' 
        L: list of integers
        dic: dictionary of key/value of ints
        return list of keys with that same value
    '''
    
    keys = []
    
    for k in dic:
        if dic[k] in L:
            keys.append(k)

    return sorted(keys)    

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    
    if not aDict:
        return []

    
    values = get_values(aDict)
    singles = get_single_nums(values)
    
    if not singles:
        return []
    else:
        return get_keys(singles, aDict)