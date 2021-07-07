#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 17:06:31 2021

@author: nebiyoumetaferia
"""

#Find the root and power of the integer 

val = int(input("Enter an integer:"))

pwr = 1 #power
root = 1 

for pwr in range(6,0, -1):    
    root = 1
    
    while(root**pwr < abs(val)):
        root+=1
    
    if(root**pwr == abs(val) and val != root):
        if(val < 0):
            print(-root, pwr)
        else:
            print(root, pwr)
        break

if(root**pwr != abs(val) or val == root):
    print("No root was found ")
        
    
        
            
            
    

