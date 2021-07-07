#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 13:57:46 2021

@author: nebiyoumetaferia
"""

#User inputs
annual_sal = float(input("Starting annual salary:"))
total_cost = 1000000.0
semi_raise = 0.07


#constants for calculation
portion_down_payment= 0.25 
current_savings = 0.0
r = 0.04
epsilon = 100.0

hi = 10000
low = 0
no_guesses = 0

#Bisection search
while (abs(current_savings - portion_down_payment*total_cost) >= epsilon and hi >= low):
   
    guess = (hi+low)//2
    temp_annual = annual_sal
    current_savings = 0.0
    
    
    for months in range(1,37):
    
        current_savings += (guess/10000)*(temp_annual/12) + current_savings*r/12
        if months % 6 == 0:
            temp_annual += semi_raise * temp_annual
    
    if(current_savings < portion_down_payment*total_cost):
        low = guess + 1
    else:
        hi = guess - 1
        
    no_guesses+=1

if(hi >= low):
    print("Best rate to save at is: ", guess/10000)
    print("Steps in bisection search:", no_guesses)
else:
    print("no solution")
      