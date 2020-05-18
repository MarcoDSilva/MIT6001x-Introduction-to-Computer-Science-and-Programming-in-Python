# -*- coding: utf-8 -*-
"""
Created on Mon May 18 22:25:29 2020
Ps1a first exercise for MIT 6.0001
@author: MarcoSilva
"""

"""
You have graduated from MIT and now have a great job! You move to the San Francisco Bay Area and
decide that you want to start saving to buy a house.  As housing prices are very high in the Bay Area,
you realize you are going to have to save for several years before you can afford to make the down
payment on a house. In Part A, we are going to determine how long it will take you to save enough
money to make the down payment 
"""


annual_salary = int(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = int(input('Enter the cost of your dream home: '))

portion_down_payment = total_cost * 0.25 #we assume 25% so 0.25
monthly_salary = annual_salary / 12
current_savings = 0

months = 0

while current_savings <= portion_down_payment:
    current_savings += (current_savings * 0.04) / 12
    current_savings += portion_saved * monthly_salary    
    months += 1


print(f'Number of months {months}')