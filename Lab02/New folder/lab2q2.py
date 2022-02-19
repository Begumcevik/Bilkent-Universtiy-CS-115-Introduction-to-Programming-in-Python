# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 08:44:53 2019

@author: begum.cevik-ug
"""

#Write a program that prompts the user for a desired sum, then repeatedly rolls two six-sided
#dice until their sum is the desired sum.

import  random 
x=random.randint(1,6)
y=random.randint(1,6)
cal=x+y
desired_sum=int(input("Enter a desired dice sum:" ))
roll=1

while desired_sum !=cal:
    roll+=1
    print(x,"and",y,"=",cal)
    x=random.randint(1,6)
    y=random.randint(1,6)
    cal=x+y

print(x,"and",y,"=",desired_sum)
print(roll,"rolls")

    


