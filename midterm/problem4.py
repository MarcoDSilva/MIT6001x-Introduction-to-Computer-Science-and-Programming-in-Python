# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 16:20:57 2020

Write a Python function that returns the sublist of strings in aList that 
contain fewer than 4 characters. For example, if aList = 
["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]

Midterm exam - problem 4

@author: MarcoSilva
"""


def lessThan4(aList):
    '''
    aList: a list of strings
    
    This function takes in a list of strings and returns a list of strings. 
    Your function should not modify aList.
    '''
    subList = []
    
    for item in aList:
        if len(item) < 4:
            subList.append(item)
    
    return subList