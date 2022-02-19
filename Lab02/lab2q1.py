# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 08:44:51 2019

@author: begum.cevik-ug
"""

#Write a program that prompts the user for an integer, calculates the factorial of the input
#integer and displays the result as a string with a comma at every third position, starting from the
#right. Assume that user input is valid. Hint: Think about representing a number as a string.

num = int(input("Enter a number: "))
fact = 1
count = 0

while num > 0:
    for i in range(num,0,-1):
        fact *= i
    break
letter = str(fact)    
ch= " " 
for i in range (len(letter)-1,-1,-1):
    ch=letter[i] + ch
    count += 1
    
    
    if (count%3) == 0 and i !=0 :
        ch="," + ch
print(num,"! =",ch)


        
        
        
        
    
    
    