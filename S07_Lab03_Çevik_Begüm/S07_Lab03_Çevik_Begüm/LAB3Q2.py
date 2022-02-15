# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 08:42:54 2019

@author: begum.cevik-ug
"""

def persistence(n):
    """
    this function calculates the number how many times my loop return  
    which is multiplicative persistence of an integer until you reach a single
    digit.
    """
    
    count=0
    multiple=n
    
    while multiple > 9:
        count += 1 
        multiple = 1
        while n > 1:
            digit = n % 10
            multiple *= digit
            n = n // 10
        n = multiple    
    return count
    
    
num = int(input("Enter an int: "))
persist = persistence(num)
print("multiplicative persistence of",num,"is",persist)



    