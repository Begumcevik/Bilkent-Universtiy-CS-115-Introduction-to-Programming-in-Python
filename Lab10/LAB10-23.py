# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 09:22:29 2019

@author: begum.cevik-ug
"""

import numpy as np
import matplotlib.pyplot as pl


arr_pop = np.loadtxt("pop_data.txt",skiprows=1)
arr_eu = arr_pop[arr_pop[:,0] == 4]


pl.figure(1)
pl.clf()
pl.subplot(2,1,1)
pl.xlabel('Gender')
pl.ylabel('Employment Rates')
pl.title('Employment Rates for Europe by Gender')
bar_width = 0.25
pl.bar(4,arr_eu[:,4], bar_width, align='edge')
pl.bar(4,arr_eu[:,5], -bar_width, align='edge')
pl.legend(['Men', 'Women'])

pl.subplot(2,1,2)
index = np.arange(0,len(arr_eu[:,0]))
male_life = arr_eu[:,1]
female_life = arr_eu[:,2]

pl.plot(index, male_life,'r:*',index,female_life,'k-.o')


pl.xlabel('Country Indexes')
pl.ylabel('Life Expectancy')
pl.legend(['Men', 'Women'])


pl.figure(2)
pl.clf()
labels = 'Male', 'Female'
male_employment = arr_pop[27,4]
female_employment= arr_pop[27,5]
ratio = male_employment,female_employment
# only "explode" the female
pl.subplot(1,2,1)
pl.pie(ratio,(0, 0.1) , labels ,autopct='%1.1f%%')
pl.title('Employment Rates for Europe by Gender in Turkey')

pl.subplot (1,2,2)
pl.title("Frequency of Gdp in Europe")
pl.hist(arr_eu[:,3],4)











