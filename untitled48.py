# -*- coding: utf-8 -*-
"""Untitled48.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y33V8CKFrkGMw7vELSv_Ith33G9-PK8r
"""

import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris.data
Y= iris.target

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size = 0.2,random_state= 42)

class KNN:
  def __init__(self,k):
    self.k = k

  def fit(self,x_train,y_train):
    self.x_train= x_train
    self.y_train = y_train

  def predict(self,X_test):
    dists = self.distance(X_test)
    pred = self.predict_label(dists)

  def distance(self,X_test):
    dist = []
    for i in X_test:
      dist.append(np.sqrt(np.sum((self.x_train - i)**2,axis =1)))
    return np.array(dist)

  def predict_label(self,dists):
    self.y_pred = []

    for i in range(len(dists)):
      indices = np.argsort(dists[i])[:self.k]
      labels,counts = np.unique(self.y_train[indices],return_counts=True)
      idx = np.argmax(counts)
      self.y_pred.append(labels[idx])

    return np.array(self.y_pred)

k = KNN(5)
k.fit(x_train,y_train)
k.predict(x_test)
prediction = k.y_pred

accuracy = accuracy_score(y_test,prediction)
accuracy
