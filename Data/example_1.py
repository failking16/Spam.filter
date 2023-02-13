# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 19:52:15 2022

@author: jksls
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import random
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/SMS-Spam-Detection/master/spam.csv", encoding= 'latin-1')
data.head()

x = np.array(data["message"])
y = np.array(data["class"])
cv = CountVectorizer()
X = cv.fit_transform(x) # Fit the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

clf = MultinomialNB()
clf.fit(X_train,y_train)

sample = input('Enter a message:')
data = cv.transform([sample]).toarray()
print(clf.predict(data))


if(count<numbers):  
    X= cv.fit_transform(spam_sample[:][0])
    X_train, X_test, y_train, y_test = train_test_split(X, spam_sample[:][1], test_size=0.33, random_state=42) 
    clf= MultinomialNB()
    clf.fit(X_train,y_train)
    
    i = 0
    while i in range(numbers):
        k=random.randint(0,len(x)-1)
        print((x[k])[:15]+"...")
        data = cv.transform([x[k]]).toarray()
        print(clf.predict(data))
        i+=1
else:
    print("U haven't mentioned any spams, so I can't work.Bye")