import numpy as np
import pandas as pd
import nltk
from nltk import stopwords
import string
from sklean.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

df = pd.read.csv("emails.csv")


x = np.array(df["message"])
y = np.array(df["class"])
cv = CountVectorizer()
X = cv.fit_transform(x) # Fit the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

clf = MultinomialNB()
clf.fit(X_train,y_train)

sample = input('Enter a message:')
data = cv.transform([sample]).toarray()
print(clf.predict(data))

df = pd.read.csv("emails.csv")
df.head()

def process(test):
    nopunc= [char for char in test if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    
    clean=[word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    return clean

message = CountVectorizer(analyzer=process).fit_transform(df['text'])
xtrain, xtest, ytrain, ytest = train_test_split(message,df['spam'],test_size=0.20,random_state=0)
classifier = MultinomialNB().fit(xtrain,ytrain)
df.drop_duplicates(inplace=True)
print(df.shape)


nltk.download("stopwords")


df('text').head().apply(process)
print(classifier.predict(xtrain))
print(ytrain.values)

pred = classifier.predict(xtrain)
print(classification_report(ytrain, pred))
print()
print("Confusion Matrix: \n", confusion_matrix(ytrain, pred))
print("Accuracy: \n", accuracy_score(ytrain, pred))

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
pred = classifier.predict(xtest)
print(classification_report(ytest, pred))
print()
print("Confusion Matrix: \n", confusion_matrix(ytest, pred))
print("Accuracy: \n", accuracy_score(ytest, pred))