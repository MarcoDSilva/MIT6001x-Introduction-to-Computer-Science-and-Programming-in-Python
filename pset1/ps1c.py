# -*- coding: utf-8 -*-
"""
Created on Wed May 20 13:37:04 2020
Pset1 , exercise 3 for MIT 6.0001s
@author: MarcoSilva
"""


"""
You have graduated from MIT and now have a great job! You move to the San Francisco Bay Area and
decide that you want to start saving to buy a house.  As housing prices are very high in the Bay Area,
you realize you are going to have to save for several years before you can afford to make the down
payment on a house. In Part C ou are now going to try to find the best rate of savings 
to achieve a down payment on a $1M house in 36 months! 
"""

#salary from user
starting_salary = float(input('Enter the starting salary: '))

#relevant data
house_total_cost =  1000000 
portion_down_payment = house_total_cost * 0.25 
semi_annual_raise = 0.07 
monthly_salary = starting_salary / 12

current_savings = 0.0

#bisection search
margin = 100
min_num = 0
max_num = 10000
rate_integer = 0

steps = 0
is_possible = True

while is_possible:
    steps += 1
    
    current_savings = 0.0
    
        
    #calculate a new num    
    rate_integer = (max_num + min_num) // 2
    
    savings_rate = rate_integer / 10000
    
    months = 1
    
    #calculating the savings with the rate that was gotten
    while months <= 36:        
        current_savings += savings_rate * monthly_salary
        current_savings += (current_savings * 0.04) / 12
        
        if months % 6 == 0:
            monthly_salary += (monthly_salary * semi_annual_raise)  
        
        months += 1
            
    #if we finally hit a tier of savings good enough we stop
    if abs(current_savings - portion_down_payment) <= margin:
        break
            
    #conditional to get a better saving ratio
    if current_savings > portion_down_payment:    
        max_num = rate_integer
    else:   
        min_num = rate_integer
        
    if min_num >= max_num:
        is_possible = False
        break
    
    print(f'bisection {steps}')
        
if is_possible:
    print(f'{steps} tried')
    print(f'savings are {current_savings}')
    print(f'ratings are {savings_rate}')
else:
    print(f'{steps} tried')
    print('error no savings possible')