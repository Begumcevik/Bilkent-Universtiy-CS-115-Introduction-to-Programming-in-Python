# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 08:54:19 2019

@author: begum.cevik-ug
"""
from matplotlib.pyplot import *
from numpy import *

clf()
temps = array([-10,-5,0,5,10,15,20,25,30 ])
dens = array ([1.341,1.316,1.293,1.269,1.247,1.225,1.204,1.184,1.164])

#find linear fit
line = polyfit(temps, dens, 1 )
#find linear fit using polyfit/polyval
value = polyval(line,temps)

xlabel('Temperature')
ylabel('Density')
title('Density of Water')
plot(temps,dens, "bo")
plot(temps,value, "r")



