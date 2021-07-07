#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 13:57:46 2021

@author: nebiyoumetaferia
"""

#User inputs
annual_sal = float(input("Starting annual salary:"))
portion_save = float(input("Portion saved:"))
total_cost = float(input("Cost of your dream home:"))
semi_raise = float(input("Semi-annual raise:"))

#constants for calculation
portion_down_payment= 0.25 
current_savings = 0.0
r = 0.04

months = 0
while(current_savings < total_cost * portion_down_payment):
    
    months += 1
    current_savings += portion_save*(annual_sal/12) + current_savings*r/12
    if months % 6 == 0:
        annual_sal += semi_raise * annual_sal

print("No of months to make downpayment is: ", months)