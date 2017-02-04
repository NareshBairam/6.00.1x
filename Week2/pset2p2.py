#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 13:44:34 2017

@author: naresh
"""



def fixedMin_util(fixed_min, balance, annualInterestRate):
    for i in range(1, 13): 
        Monthly_interest_rate = (annualInterestRate) / 12.0
        Monthly_unpaid_balance = (balance) - (fixed_min)
        balance = (Monthly_unpaid_balance) + (Monthly_interest_rate * Monthly_unpaid_balance)
        
        if(balance < 0):
            return 1

def fixedMin(): 
    balance = 4773
    annualInterestRate = 0.2
    fixed = 10
    while(fixed < balance):
        bal = fixedMin_util(fixed, balance, annualInterestRate)
        if(bal == 1):
            print("Lowest Payment: %d" % fixed)
            return 
        else:
            fixed = fixed + 10
            
            
fixedMin()
    
        