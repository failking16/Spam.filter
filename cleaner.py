# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:03:50 2023

@author: jksls
"""

import numpy as np
import pandas as pd
import defin as dfn
import importlib
import re

df = pd.read_csv('Data\emails.csv')
importlib.reload(dfn)

replacement=df['spam'].replace({1:0,'':0})
df = df.replace(['/','-','\+',':',';','!','  ','   ','the','The','and','or','not',],' ',regex=True)
df['text'] = df['text'].str[8:]
df['spam']=replacement

x = np.array(df['text'])
length=0
number = r'[0-9]'

for length in range(len(df['text'])):
    x[length]=x[length].lower()
    x[length]=re.sub(number,'',x[length])
    length+=1

dfn.erasing('change.csv')
df['text'] = x

df.to_csv('Data\change.csv')

#this code is used to take data, where some messages were previously marked as spam, to clarify it,
#because I want to write a code that will find out the patterns of the spam messages.
#for this I think it is better when it is starting the work with the clear data.