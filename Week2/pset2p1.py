#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 00:23:03 2017

@author: naresh
"""

#balance = 484
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

for i in range(1, 13):
    Monthly_interest_rate= (annualInterestRate)/12.0
    Minimum_monthly_payment = (monthlyPaymentRate)*(balance)
    Monthly_unpaid_balance = balance - Minimum_monthly_payment
    balance = (Monthly_unpaid_balance) + (Monthly_interest_rate * Monthly_unpaid_balance)
print("Remaining balance: %.2f" % balance )
