# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 19:26:56 2020
Write a Python function that takes in two lists and calculates whether they are permutations of each other. 
The lists can contain both integers and strings. We define a permutation as follows:
    
    - the lists have the same number of elements
    - list elements appear the same number of times in both lists

If the lists are not permutations of each other, the function returns False.
If they are permutations of each other, the function returns a tuple consisting of the following elements:

    the element occuring the most times
    how many times that element occurs
    the type of the element that occurs the most times

@author: MarcoSilva
"""

def get_dic(L):   
    '''
    ----------
    L : a list of integer / strings

    Returns
    -------
    dic : a dictionary that contains the number of times X element showed up in the list

    '''
    dic = {}
    for el in range(len(L)):        
        element = L[el]
        
        if dic.get(element, -1) < 0:
            dic[element] = 1
        else:
            dic[element] += 1

    return dic



def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    
    # verifying if lists have the same size
    if not len(L1) == len(L2):
        return False

    # verifying if lists are empty
    if not len(L1) and not len(L2):
        return (None, None, None)
    
    # we get the dictionaries with the number of occurences from both lists
    dic1 = get_dic(L1)
    dic2 = get_dic(L2)            
            
    # comparing the equality between both lists    
    for key in dic1:
        if not dic1[key] == dic2[key]:
            return False
        

    most_results = ['', 0, None]
    # now that we know they are equal, we pick the maximum value and return it    
    for key in dic1:    
        if dic1[key] > most_results[1]:
            most_results[0] = key
            most_results[1] = dic1[key]
            most_results[2] = type(key)
            
    return (most_results[0], most_results[1], most_results[2])
    
    
    
    
    