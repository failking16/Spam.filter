# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 11:32:50 2023

@author: jksls
"""

import numpy as np
import pandas as pd
import defin as dfn
import importlib

importlib.reload(dfn)
df = pd.read_csv('Data\emails.csv')

dfn.erasing('index.csv')
dfn.cleaning_1()

spam_indeces = np.array(df['spam'])
spam_context = np.array(df['text'])

index = 0
length = 0

for length in range(len(spam_indeces)):
    if spam_indeces[length]!=1 :
        break
    else:
        length+=1

spam_example = dfn.randomiser(0,length)
spam_set = dfn.randomiser(length+1,len(spam_indeces)-1)
spam_tracker = np.array([])

print("\nYour spam indexes:\n",spam_example)
