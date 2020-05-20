# -*- coding: utf-8 -*-
"""
Created on Mon May 19 20:12:11 2020
Ps1b second exercise for MIT 6.0001
@author: MarcoSilva
"""


"""
You have graduated from MIT and now have a great job! You move to the San Francisco Bay Area and
decide that you want to start saving to buy a house.  As housing prices are very high in the Bay Area,
you realize you are going to have to save for several years before you can afford to make the down
payment on a house. In Part B, you are an MIT graduate, and clearly you are going 
to be worth more to your company over time! 
"""


annual_salary = int(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = int(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

portion_down_payment = total_cost * 0.25 #we assume 25% so 0.25
monthly_salary = annual_salary / 12
current_savings = 0

months = 0

while current_savings <= portion_down_payment:
    current_savings += (current_savings * 0.04) / 12
    current_savings += portion_saved * monthly_salary        
    months += 1
    
    if months % 6 == 0:
        monthly_salary = monthly_salary + (monthly_salary * semi_annual_raise)


print(f'Number of months {months}')