# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:09:52 2023

@author: jksls
"""

import numpy as np
import pandas as pd
import random
import re


def erasing(name):
    f = open('Data/'+name,"w+")
    f.close()


def randomiser(min,max):
    i=0
    index_list=np.array([])
    
    for i in range(10):
        rand=random.randint(min,max)
        index_list= np.append(index_list,rand)
        
    return index_list


def cleaning_1():
    df = pd.read_csv('Data\emails.csv')
    df['spam'] = df['spam'].replace([1,''],0)
    df = df.replace(['/','-','\+',':',';','!','  ','   ','the','The','and','or','not',],' ',regex=True)
    df['text'] = df['text'].str[8:]
    x = np.array(df['text'])
    number = r'[0-9]'
    length=0
    for length in range(len(df['text'])):
        x[length]=x[length].lower()
        x[length]=re.sub(number,'',x[length])
        length+=1
    df['text']=x
    df.to_csv('Data\change.csv')


