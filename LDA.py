# -*- coding: utf-8 -*-
"""Untitled48.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y33V8CKFrkGMw7vELSv_Ith33G9-PK8r
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class LDA:


  def formula(self,X,cov_matrix,mean,PR_k):
    cov_mat_inv = np.linalg.inv(cov_matrix)
    sigma = (X.dot(cov_mat_inv)).dot(mean) -0.5*(mean.T.dot(cov_mat_inv)).dot(mean) + np.log(PR_k)
    return sigma


  def fit(self,x_train,y_train):
    self.cov_matrix = None
    self.full_stats = {}
    classes,counts = np.unique(y_train,return_counts = True)

    for i in range(len(classes)):
      class_stats = {}

      x_i = x_train[y_train == classes[i]]
      class_stats['mean'] = np.mean(x_i , axis = 0)
      class_stats['PR_k'] = counts[i]/len(x_train)

      if self.cov_matrix is None:
        self.cov_matrix = ((x_i-class_stats['mean']).T).dot((x_i-class_stats['mean']))
      else:
        self.cov_matrix + ((x_i-class_stats['mean']).T).dot((x_i-class_stats['mean']))

      self.full_stats[classes[i]] = class_stats

    self.cov_matrix = self.cov_matrix/(len(x_train) - len(counts))

    return


  def predict_prob(self,X_test):
    pred_prob = []
    for item in self.full_stats.values():
      pred_prob.append(self.formula(X_test,self.cov_matrix,item['mean'],item['PR_k']))
    return np.array(pred_prob).T


  def pred_labels(self,x_test):
    y_pred = np.argmax(self.predict_prob(x_test),axis = 1)
    return y_pred

iris = load_iris()
X = iris.data
Y = iris.target
x_train, x_test, y_train, y_test= train_test_split(X, Y,test_size = 0.3, random_state=42)
lda = LDA()
lda.fit(x_train, y_train)
predictions = lda.pred_labels(x_test)

accuracy = accuracy_score(predictions,y_test)
print(f'accuracy = {accuracy}')

