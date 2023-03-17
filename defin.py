# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:09:52 2023

@author: jksls
"""

import numpy as np
import pandas as pd
import random
import nltk
import re
from sklearn.feature_extraction.text import CountVectorizer


def CountVector(array,size):
    cv = CountVectorizer()
    cv.fit_transform(array)
    

def erasing(name):
    f = open('Data/'+name,"w+")
    f.close()


def remove_prepositions(text):
    prepositions = ['at', 'by', 'for', 'from', 'in', 'of', 'on', 'to', 'with','the','a','are','is','am','but','and','or','out']
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in prepositions]
    return ' '.join(filtered_words)


def randomiser(min,max):
    arr = np.array([random.randint(min, max) for _ in range(10)])
    return arr


def cleaning_1():
    df = pd.read_csv('Data\emails.csv')
    df['spam'] = df['spam'].replace([1,''],0)
    df['text'] = df['text'].str[8:]
    x = np.array(df['text'])
    number = r'[0-9]'
    length=0
    for length in range(len(df['text'])):
        x[length]=x[length].lower()
        x[length]=remove_prepositions(x[length])
        x[length]=re.sub(number,'',x[length])
        length+=1
    df['text']=x
    df.to_csv('Data\change.csv')
    
    
def cleaning_sample(array):
    length=0
    for length in range(len(array)):
        array[length] = filter_english_words(array[length])
        length+=1
    return array


def filter_english_words(text):
    nltk.download('words')
    words = text.split()
    english_words = [word for word in words if word.lower() in nltk.corpus.words.words()]
    return ' '.join(english_words)

def countng(vocabulary):
    