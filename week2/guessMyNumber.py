# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 00:43:53 2020
Exercise: guess my number
the user thinks of an integer between 0 (inclusive) and 100 (not inclusive).
the computer makes guesses, and you give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's secret number!
@author: MarcoSilva
"""

print("Please think of a number between 0 and 100!")

low = 0
high = 100
number_found = False
guess = int((low + high) / 2)

while not number_found:  
    
    print(f'Is your secret number {guess}?')
    verify_correct_number = input("Enter 'h' to indicate the guess is too high." 
                                 "Enter 'l' to indicate the guess is too low."
                                 "Enter 'c' to indicate I guessed correctly. ")
    
    if verify_correct_number == 'h':
        high = guess
    elif verify_correct_number == 'l':
        low = guess
    elif verify_correct_number == 'c':
        number_found = True
    else:
        print("Sorry, I did not understand your input.")
        continue
    
    guess = int((low + high) / 2)
    
print(f'Game over. Your secret number was: {guess}')
    