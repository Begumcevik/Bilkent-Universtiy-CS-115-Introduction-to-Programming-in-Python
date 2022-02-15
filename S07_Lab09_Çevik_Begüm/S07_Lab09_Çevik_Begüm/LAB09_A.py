# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:14:27 2019

@author: begum.cevik-ug
"""
from Friends import *
import calendar
import datetime


def sort_surname (L):
    """
    takes a list of Friends as a parameter. Using the selection
    sort algorithm sorts the Friends in descending order of their surname (Z-A) 
    """
    suffixStart = 0
    while suffixStart != len(L):
        for i in range (suffixStart, len(L)):    #len(L)-1+1
            if L[i].get_surname() > L[suffixStart].get_surname():
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1
     
def find_friend (L,starting_index,month):
    """
    takes a list of Friends, a starting index and the month. 
    Using a recursive linear search algorithm, searches the list and
    displays all Friends who have birthdays in the given month. 
    """ 
    
    if starting_index == len(L):
        return False
    elif L[starting_index].get_birthday().month == month:
        print(L[starting_index])
        starting_index += 1
        return find_friend(L,starting_index,month)
    else:
        return find_friend(L,starting_index+1,month)  
    
def load_friends (filename, Empty):
    """
    function takes a filename and an empty list as parameters.
    The function should read the data from the file, create Friends from the file and
    add them to the list
    """
    
    file = open(filename,'r')
    for line in file:
        line = line.strip()
        line = line.split()
        fname = line[0]
        surname = line[1]
        birth_date = line[2]
        phone = line[3]
        Empty.append(Friend(fname, surname,birth_date,phone))
    file.close()  
    return Empty

Empty=[]
List_info = load_friends('birthday_list.txt', Empty)

print('Friends:' , '\n')
print(List_info)
    
print ('Friends by descending birthday:' + '\n')
List_info.sort(reverse = True)
print (List_info)

print ('Friends by descending surname:' + '\n')
sort_surname(List_info)
print (List_info)

current_month = calendar.month_name[datetime.datetime.today().month-3]
print("Friends with birthdays in:" ,current_month)
find_friend(List_info,0,datetime.datetime.today().month-3)



