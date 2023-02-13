# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 20:25:53 2022

@author: jksls
"""

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import random

df = pd.read_csv('emails.csv')
df.head()

x = np.array(df['text'])
y = np.array(df['spam'])

cv = CountVectorizer()

numbers = int(input("number of messages ="))
message_list = np.array([])
spam_sample = np.empty((numbers,2)) 
i=0
count=0

while i in range(numbers):
    k=random.randint(0,len(x)-1)
    message_list=np.append(message_list,k)
    print(x[k])
    i+=1
    l=int(input("Is it spam or no? (answer 1/yes or 0/no)"))
    if l==1:
        l_1 = input("what are the words(sentences) showed u that it is spam?")
        spam_sample=np.vstack(spam_sample,np.array([[l_1,l]]))
    else:
        spam_sample=np.vstack(spam_sample,np.array([[x[k],l]]))
        count+=1
    
print(spam_sample)

