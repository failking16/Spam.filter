# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 11:32:50 2023

@author: jksls
"""

import numpy as np
import pandas as pd
import defin as dfn
import importlib
from sklearn.feature_extraction.text import CountVectorizer

importlib.reload(dfn)

dfn.erasing('index.csv')
dfn.cleaning_1()
cv = CountVectorizer()

df = pd.read_csv('Data\emails.csv')
cf = pd.read_csv('Data\change.csv')

spam_indeces = np.array(df['spam'])
spam_context = np.array(cf['text'])

index = 0
length = 0

for length in range(len(spam_indeces)):
    if spam_indeces[length]!=1 :
        break
    else:
        length+=1

spam_example = dfn.randomiser(0,length)
spam_set = dfn.randomiser(length+1,len(spam_indeces)-1)
spam_example_text = spam_context[spam_example]

print("\nYour spam indexes:\n",spam_example)
print(spam_example_text[1])
spam_contexts=dfn.cleaning_sample(spam_example_text)

print(spam_example_text[1])

for index in range(10):
    spam_example_text[index]= spam_example_text[index]
    index+=1

Spam_list = list(spam_example_text)
cv.fit_transform(Spam_list)

filtered_vocab = {k:v for k,v in sorted(cv.vocabulary_.items(), key=lambda x:x[1]) if v >= 80}
Z= np.array(filtered_vocab.keys())
Y= np.array(filtered_vocab.values())



