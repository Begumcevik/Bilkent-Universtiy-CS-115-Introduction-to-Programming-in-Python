# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 09:21:38 2019

@author: begum.cevik-ug
"""
from Country import *
c_list = []
file1 = open("countries.txt","r")

for line in file1:
    line=line.rstrip()
    variable = line.split(",")
    cname = variable[0]
    region = variable[1]
    expectancy = (float(variable[4]) + float(variable[5])) / 2
    education = (float(variable[2]) + float(variable[3])) / 2
    literacy = (200-(float(variable[6]) + float(variable[7]))) / 2
    c_list.append(Country(cname,region,education,literacy,expectancy))
    

c_list.sort()
print(c_list)


iregion = input("Enter a region: ")
iexpectancy = int(input("Enter a life expectancy limit: "))
print("Countries in" , iregion , "with life expectancy above " , iexpectancy )   

allsum=0
count=0
for j in c_list:
    if j.getregion()  == iregion  :
        allsum += j.getliteracy()
        count+=1
        if j.getexpectancy() > iexpectancy:
            print(j.getcname())
average=allsum/count
print("Average literacy in ", iregion , ": {0:.2f}".format(average))