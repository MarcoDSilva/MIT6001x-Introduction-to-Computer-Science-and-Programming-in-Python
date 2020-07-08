# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 21:37:49 2020

@author: MarcoSilva
"""


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, other):
        ''' return if coordinates refer to the same point in the plane '''
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        ''' returns a string that looks like a valid python expression
            that could be used to recreate an object with the same value.
        '''
        return "Coordinate(" + str(self.x) + "," + str(self.y) + ")"
    