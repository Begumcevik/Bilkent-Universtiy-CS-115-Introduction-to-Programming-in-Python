# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 08:42:56 2019

@author: begum.cevik-ug
"""

import random
def flipCoinUntil_X_Heads(x):
    """
    function named flipCoinUntil_X_Heads(x) that takes integer x
    (x > 0) as parameter and repeatedly flips a coin until x heads in a row are seen.
    this function gives random value (0-for T nad 1-for H) then find how many head in a row with 
    increasing number of heads
    """
    noheads=0
    noflips=0
    while noheads < x:
        prob=random.randint(0,1)
        #0-for T nad 1-for H
        if prob == 0:
            print("T",end='') 
            noheads=0
        else:
            print("H",end='')
            noheads+=1
        noflips+=1
    return noflips
noheads = int(input("Enter how many heads you want in a row:  "))


while noheads > 0:
   num=flipCoinUntil_X_Heads(noheads)
   print()
   print(noheads,"heads in a row")
   print(num,"coin flips in total")
   noheads=int(input("Enter how many heads you want in a row:  "))
 
print("non positive integer... Bye!")       