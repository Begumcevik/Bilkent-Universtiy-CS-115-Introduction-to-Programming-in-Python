# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Write a program that prompts the user to read in two input values: a number of feet,
#followed on a separate line by a number of inches. The program should convert this
#amount to centimeters. Assume that all input values are ints. 1 foot is 12 inches and
#1 inch is 2.54 centimeter. Here is a sample run of the program.


feet=int(input("Enter a number of feet: "))
inches=int(input("Enter a number of inches: "))
#convert into centimeters
total= (feet*12*2.54) + (inches*2.54)
print("{0:2d} feet and {1:2d} inches = {2:5.2f} cm".format(feet,inches,total))









    


    


    

    
    

    
    



