#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 17:43:57 2017

@author: naresh
"""

#balance = 4773
#annualInterestRate = 0.2

#Monthly_interest_rate = (annualInterestRate) / 12.0
#Monthly_payment_lower_bound = balance / 12
#Monthly_payment_upper_bound = (balance * (1 + Monthly_interest_rate)**12) / 12.0

 
def fixedMin_util(fixed_min, balance, annualInterestRate):
    for i in range(1, 13): 
        Monthly_interest_rate = (annualInterestRate) / 12.0
        Monthly_unpaid_balance = (balance) - (fixed_min)
        balance = (Monthly_unpaid_balance) + (Monthly_interest_rate * Monthly_unpaid_balance)
    return balance

def fixedMin(): 
    balance = 320000
    annualInterestRate = 0.2
   # epsilon = 0.01
    Monthly_interest_rate = (annualInterestRate) / 12.0
    Monthly_payment_lower_bound = balance / 12
    Monthly_payment_upper_bound = (balance * ((1 + Monthly_interest_rate)**12)) / 12.0
 
    bal = 1

    fixed = (Monthly_payment_lower_bound + Monthly_payment_upper_bound)/2.0
    while(bal):
        bal = fixedMin_util(fixed, balance, annualInterestRate)

        if(bal > 0 and bal <= 0.1):
            print("Lowest Payment: %.2f" % fixed)
            return 
        if(bal < 0.00):
            Monthly_payment_upper_bound = fixed
        else:
            Monthly_payment_lower_bound = fixed
        
        fixed = (Monthly_payment_lower_bound + Monthly_payment_upper_bound)/2.0
            
            
            
fixedMin()