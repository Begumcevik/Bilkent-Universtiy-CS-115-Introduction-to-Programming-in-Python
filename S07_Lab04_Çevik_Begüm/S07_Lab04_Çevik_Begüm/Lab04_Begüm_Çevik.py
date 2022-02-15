# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 08:42:55 2019

@author: begum.cevik-ug
"""
import ed_functions

file1 = open('education.txt','r')
# inputs a tuple of two character strings 
char1,char2 = input("Enter start and end characters: ")
upperch1=char1.upper()
upperch2=char2.upper()

filename = char1 + 'to' + char2 + '_edual_ed.txt' 
outfile=open(filename,'w')

for line in file1:
    ch=line[0]
    male_education_rate,female_education_rate = ed_functions.get_levels(line)
    tf_relation = ed_functions.same_education(male_education_rate,female_education_rate)
    
    
    if tf_relation is True and upperch1 <= ch <=upperch2:
        output=ed_functions.get_country_region(line)
        outfile.write(output[0] + "\t" + output[1] + "\n" )
        
outfile.close()
file1.close()
