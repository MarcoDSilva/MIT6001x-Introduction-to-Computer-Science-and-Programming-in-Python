# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 15:07:34 2020

write a program that calculates the minimum fixed monthly payment needed 
in order pay off a credit card balance within 12 months
with Bisection Search to make the program faster

@author: MarcoSilva
"""

#this function isn't needed per se, but for clarity I prefer to use it
def roundNum(num):
    ''' 
    num : int or float
    returns: float w 2 decimal case number.
    '''
    return round(num, 2)

#these 2 variables are used by the tester
balance = 320000
annualInterestRate = 0.2

monthly_interest = (annualInterestRate) / 12.0
lower_bound = roundNum(balance / 12)
upper_bound = roundNum((balance * ((1 + monthly_interest) * 12)) / 12.0)

min_payment = roundNum((lower_bound + upper_bound / 2))
found = True

#we loop 'til we find the value in the margin specified (0.1 in this case)
while(found):
    temp_balance = balance    
    
    # calculate the balance after the payment and the interest
    for month in range(1,13):
        temp_balance -= min_payment
        temp_balance += (monthly_interest * temp_balance)
    
    # if the balance is negative or positive (higher than our margin)
    # we specify new values to the bounds
    if temp_balance < 0.1:
        upper_bound = min_payment
    elif temp_balance > 0.1:
        lower_bound = min_payment  
        
    # if both bounds are below our margin, we found the minimum value required
    # to pay the debt in 1 year
    if abs(upper_bound - lower_bound) <= 0.01:
        break
    
    min_payment = roundNum((lower_bound + upper_bound) / 2)

print('Lowest Payment: ' + str(min_payment))