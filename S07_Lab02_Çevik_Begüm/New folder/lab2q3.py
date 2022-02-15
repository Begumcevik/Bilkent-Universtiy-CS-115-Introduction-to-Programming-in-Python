# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 08:44:53 2019

@author: begum.cevik-ug
"""

#Write a program that prompts the user for an integer and returns the number of even-valued digits
#in the specified number. An even-valued digit is either 0, 2, 4, 6, or 8. Assume that the input values
#are either a positive or a negative integer until 0 is entered by the user.

num = int(input("Enter an integer until 0: "))
count = 0
while num != 0: 
   a = abs(num)
   b = str(a)
        
   even = 0
   for i in b:
        i = int(i)
        if (i%2) == 0 and i != 0:
            even += 1 
            
   print(num,"has",even,"even digits")
        
   num = int(input("Enter an integer until 0: ")) 
        
print("good bye!!")

        

            
        
        
        



