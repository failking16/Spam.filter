# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 11:32:50 2023

@author: jksls
"""

import numpy as np
import pandas as pd
import random

def randomiser(min,max):
    i=0
    index_list=np.array([])
    
    for i in range(10):
        rand=random.randint(min,max)
        index_list= np.append(index_list,rand)
        
    return index_list

def analyse():
    
    return

df = pd.read_csv('Data\emails.csv')

cleaning = open('Data\index.csv','w+')
cleaning.close()

spam_indeces = np.array(df['spam'])
spam_context = np.array(df['text'])

index = 0
length = 0

for length in range(len(spam_indeces)):
    if spam_indeces[length]!=1 :
        break
    else:
        length+=1

spam_example = randomiser(0,length)
spam_set = randomiser(length+1,len(spam_indeces)-1)
spam_tracker = np.array([])

print("\nYour spam indexes:\n",spam_example)

