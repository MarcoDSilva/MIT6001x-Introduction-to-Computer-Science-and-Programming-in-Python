# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 19:06:33 2020

Write a program to calculate the credit card balance after one year 
if a person only pays the minimum monthly payment 
required by the credit card company each month.

PSET 1 of week 2
@author: MarcoSilva
"""

#these 3 variables are used by the tester
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#variables to calculate the monthly rate
monthlyInterestRate = annualInterestRate / 12.0

#cycle for the monthly payments
for month in range(1,13):
    minimumMonthlyPayment = monthlyPaymentRate * balance    
    monthlyUnpaidBalance = balance - minimumMonthlyPayment    
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    
print('Remaining balance: ' + str(round(balance, 2)))

 