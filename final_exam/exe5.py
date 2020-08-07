# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 22:39:22 2020
You are given the following superclass Container.
Write a class that implements the specifications below. 
Do not override any methods of Container.
@author: MarcoSilva
"""


class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s
    

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        for k in self.vals:
            if k == e:
                self.vals[k] -= 1

                    
    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. 
        """
        for k in self.vals:
            if k == e:
                return self.vals[k]
            
        return 0