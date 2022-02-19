# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 09:26:02 2019

@author: begum.cevik-ug
"""

#Write a program that inputs three integers from the user and reports whether or not if
#one of the integers is the midpoint between the other two integers (exactly halfway
#between the other two integers). the midpoint could be the first, second or third one.
    
first= int(input("Enter an integer: "))
second= int(input("Enter an integer: "))
third= int(input("Enter an integer: "))

if second < first:
    first,second = second, first
if second > third:
    second,third=third, second 
if second < first:
    second, first= first,second  
print(first,second,third)

if second-first == third-second:
    print("{1:2d} is the midpoint of {0:2d},{1:2d},{2:2d}".format(first,second,third))
else: 
    print("there is no midpoint among {0:2d},{1:2d},{2:2d}".format(first,second,third))
     
       
       

    
    