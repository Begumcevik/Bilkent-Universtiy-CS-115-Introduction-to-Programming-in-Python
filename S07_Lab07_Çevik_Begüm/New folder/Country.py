# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Country( object ):
    def __init__(self,cname,region,education,literacy,expectancy):
        self.__cname = cname
        self.__region = region
        self.__education = education
        self.__literacy = literacy
        self.__expectancy = expectancy
        
    def getcname(self):
        return self.__cname
        
    def getregion(self):
        return self.__region
    
    def geteducation(self):
        return self.__education
    
    def getliteracy (self):
        return self.__literacy
    
    def getexpectancy(self):
        return self.__expectancy
   
    def seteducation(self, education):
        self.__education = education
        
    def setliteracy(self, literacy):
        self.__literacy = literacy
        
    def setexpectancy(self, expectancy):
        self.__expectancy = expectancy
           
    def __repr__(self):
        return ("\n\n" + self.__cname +"("+self.__region + "):" +'\n Life expectancy: {0:.2f}'.format(self.__expectancy)+'\n Literacy Rate: {0:.2f}'.format(self.__literacy) + '\n Education Rate: {0:.2f}'.format(self.__education))
        
    def __lt__(self,other):
        if self.getregion() < other.getregion():
            return True
        elif self.getregion() == other.getregion():
            return self.getliteracy() < other.getliteracy()
        else: 
            return False
    
            
   

        
    
    
    
        
        
        
        
   
       
     
