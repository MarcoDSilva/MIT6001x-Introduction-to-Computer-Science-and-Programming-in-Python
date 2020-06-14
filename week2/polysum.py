# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 18:34:58 2020

Write a function called polysum that takes 2 arguments, n and s. 
This function should sum the area and square of the perimeter of the regular polygon. 
The function returns the sum, rounded to 4 decimal places.

@author: MarcoSilva
"""

import math

def area(n,s): 
    '''  
    n : int -  number of sides.
    s : float/int - size of the sides of a polygon.
    Returns - polygon_area : float
    '''
    
    polygon_area = (0.25 * n * (s ** 2)) / math.tan(math.pi / n)
    return polygon_area

def perimeter(n,s):
    '''
    n : int -  number of sides.
    s : float/int - size of the sides of a polygon.
    Returns - poly_perimeter : float
    '''
    poly_perimeter = s*n
    return poly_perimeter

def polysum(n,s):
    '''
    n : int -  number of sides.
    s : float/int - size of the sides of a polygon.
    Returns - the sum of the area of a regular polygon and the perimeter
        rounded to 4 decimal houses
    '''
    sum = float(area(n,s) + perimeter(n,s) ** 2)
    return round(sum, 4)