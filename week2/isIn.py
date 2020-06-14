# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 14:42:57 2020

determine if a character is in a string, so long as the string 
is sorted in alphabetical order. 

@author: MarcoSilva
"""


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise    '''    
    
    if aStr == '':
        return False  
            
    middle = len(aStr) // 2
    
    if char == aStr[middle]:
        return True

    elif char < aStr[middle]:
        return isIn(char, aStr[:middle])
        
    elif char > aStr[middle]:            
        return isIn(char, aStr[middle:])  
    
    return False


