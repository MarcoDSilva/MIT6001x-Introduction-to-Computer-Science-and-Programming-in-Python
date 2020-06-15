# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 21:54:31 2020

write a program that calculates the minimum fixed monthly payment needed 
in order pay off a credit card balance within 12 months

The monthly payment must be a multiple of $10 

Pset 2 of week 2
@author: MarcoSilva
"""


#these 2 variables are used by the tester
balance = 3926
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
debt = True

minimumPayment = 10

while debt:
    tempBalance = balance
    
    for month in range(1,13):
        monthlyUnpaidBalance = tempBalance - minimumPayment
        tempBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        
    if tempBalance <= 0:
        debt = False
    else:
        minimumPayment += 10

print('Lowest Payment: ' + str(minimumPayment))