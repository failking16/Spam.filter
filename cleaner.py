# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:03:50 2023

@author: jksls
"""

import pandas as pd

df = pd.read_csv('Data\emails.csv')

replacement=df['spam'].replace({1:0,'':0})
#replacement1 = df.replace(['/','-','+',':',';','!'],' ',regex=True)
df = df.replace(['/','-','\+',':',';','!','  ','   '],' ',regex=True)
df['spam']=replacement

f = open('Data\change.csv',"w+")
f.close()

df.to_csv('Data\change.csv')

#this code is used to take data, where some messages were previously marked as spam, to clarify it,
#because I want to write a code that will find out the patterns of the spam messages.
#for this I think it is better when it is starting the work with the clear data.