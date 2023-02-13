# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 11:32:50 2023

@author: jksls
"""

import numpy as np
import pandas as pd
import random

df = pd.read_csv('Data\emails.csv')

cleaning = open('Data\index.csv','w+')
cleaning.close()

spam_indeces = np.array(df['spam'])
spam_context = np.array(df['text'])

index = 0

for index in range(10):
    size = random.randint(0,len(df['spam']-1))
    