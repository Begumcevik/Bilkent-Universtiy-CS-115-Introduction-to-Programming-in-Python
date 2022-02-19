# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
this func. takes a string and returns the float m_ed and f_ed.
"""

def get_levels (line) :
    tab1 = line.find("\t")
    tab2 = line.find("\t",tab1+1)
    tab3 = line.rfind("\t")
    
    m_ed = line[tab2:tab3]
    f_ed = line[tab3:len(line)]
    
    m_ed = float(m_ed)
    f_ed = float(f_ed)
    
    return(m_ed,f_ed)

"""
this func. takes two float education values, and returns True
if their rounded values are the same, False if different.
"""
def same_education (m_ed,f_ed) :
    if round(m_ed) == round(f_ed):
        return True
    else:
        return False
"""    
def same_education (m_ed,f_ed) :
    rem_m_ed = m_ed % int(m_ed)
    rem_f_ed = f_ed % int(f_ed)
    
    if rem_m_ed >= 0.5:
        m_ed=int(m_ed)+1
    elif rem_m_ed < 0.5:
        m_ed=int(m_ed)
        
    if rem_f_ed >= 0.5:
        f_ed=int(f_ed)+1
    elif rem_f_ed < 0.5:
        f_ed=int(f_ed)
        
    if f_ed == m_ed:
        return True
    else:
        return False
       
"""    

"""
this func. takes a string containing the country data and
returns the country and the region in the string.
"""

def get_country_region (line) :
    region_starting = line.find("\t")
    region_ending = line.find("\t",region_starting+1)
    region = line[region_starting+1 : region_ending]
    
    country = line[0:region_starting]
    
    return(country,region)
        

    
    


