# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 09:26:02 2019

@author: begum.cevik-ug
"""

#Write a program that inputs a month from the user (an integer between 1 and 12)
#and displays the number of days in that month. For example, if the input month is 9
#for September, it should display 30 because September has 30 days.
#Assume that the code is not being run during a leap year (that February always has
#28 days). The following are the number of days in each month: 

month=int(input("Enter a number of month as a integer(in range 1-12): "))
if month ==1 or month ==3 or month ==5 or month ==7 or month ==8 or month ==10 or month ==12:
    print("The month {0:1d} has 31 days".format(month))
elif month ==2:
    print("The month {0:1d} has 28 days".format(month))
elif month ==4 or month ==6  or month ==9 or month ==11: 
    print("The month {0:1d} has 30 days".format(month))
else:
    print("Your input is invalid!!!")