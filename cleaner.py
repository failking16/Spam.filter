# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:03:50 2023

@author: jksls
"""

import numpy as np
import pandas as pd

df = pd.read_csv('Data\emails.csv')

replacement=df['spam'].replace({1:0,'':0})
#replacement1 = df.replace(['/','-','+',':',';','!'],' ',regex=True)
df = df.replace(['/','-','\+',':',';','!','  ','   '],' ',regex=True)
df['text'] = df['text'].str[8:]
df['spam']=replacement

x = np.array(df['text'])
length=0

for length in range(len(df['text'])):
    x[length]=x[length].lower()
    length+=1

f = open('Data\change.csv',"w+")
f.close()

df.to_csv('Data\change.csv')

#this code is used to take data, where some messages were previously marked as spam, to clarify it,
#because I want to write a code that will find out the patterns of the spam messages.
#for this I think it is better when it is starting the work with the clear data.