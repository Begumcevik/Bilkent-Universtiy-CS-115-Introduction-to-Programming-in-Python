# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import datetime

class Friend:
    
    def __init__(self, fname, surname, birth_date, phone):
        self.__fname = fname
        self.__surname = surname
        self.__phone_number = phone
        self.__birthday = datetime.datetime.strptime(birth_date, '%Y-%m-%d').date()        
   
    def get_fname(self):
        return self.__fname
    
    def get_surname(self):
        return self.__surname
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_birthday(self):
        return self.__birthday
    
    def set_birthday(self, birthday2):
        self.__birthday = datetime.datetime.strptime(birthday2, '%Y-%m-%d').date()
    
    def __lt__(self,other):
        return self.__birthday < other.__birthday

    def __repr__(self):
        return "\n" +'(' + self.__surname + ')' + '\t'+ self.__fname + '\t' + str(self.__birthday) + '\t' + '(' + self.__phone_number + ')'



