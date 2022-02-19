# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 08:42:57 2019

@author: begum.cevik-ug
"""
#this function find odd integer in given range
import random
def randomOdd(lower_range,upper_range):
    """
    input :lower_range and upper_range are the bound
    returns  again if random numbers are divisible by 2, 
    oteherwise add this number in the string
    """
    ran = random.randint(lower_range,upper_range)
    
    while (ran%2) == 0:
        ran = random.randint(lower_range,upper_range)
    return ran   
    
    
lower = int(input("Enter the lower bound of the range: "))
upper = int(input("Enter the upper bound of the range: "))
count = int(input("How many odd integers do you want in this range: "))
ch= " "
for i in range (0,count):
    ran = randomOdd(lower,upper)
    ch= ch + str(ran) +" " 
    
print("Here are",count,"random odd integers in range[",lower,",",upper,"]:",ch)
