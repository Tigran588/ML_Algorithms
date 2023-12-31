# -*- coding: utf-8 -*-
"""Untitled46.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NQ8y_uFOuekKX01uKHi-nb934Fs7wGlL
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.DataFrame(
    {
    'x':[0,1,4,2,0,1,3,7,6],
    'y':[1,1,0,3,5,6,6,4,8]})

X = data.values

class HierarchicalCLastering:
  def __init__(self,num_clusters,dist_func,linkage = 'single',distance_threshold = None):
    self.num_clusters = num_clusters
    self.dist_func = dist_func
    self.linkage = linkage
    self.distance_threshold = distance_threshold

  def fit(self,X):
    clusters = []
    for item in X:
      clusters.append([item])

    while len(clusters) > self.num_clusters :
      ClusterDistance =  []
      for i in range(len(clusters)):
        for j in range(i+1,len(clusters)):
          dist = []
          for c1 in clusters[i]:
            for c2 in clusters[j]:
              dist.append(self.dist_func(c1,c2))
            if self.linkage == 'single':
              ClusterDistance.append([i,j,np.min(dist)])
            elif self.linkage == 'complete':
              ClusterDistance.append([i,j,np.min(dist)])
            else:
              ClusterDistance.append([i,j,np.sum(self.distances)/len(dist)])

      near = ClusterDistance[0]
      for i in ClusterDistance:
        if i[-1] < near[-1]:
          near = i
      if near[-1] > self.distance_threshold:
        break
      clusters[near[0]].extend(clusters[near[1]])
      del clusters[near[1]]
      self.k = len(clusters)

c = HierarchicalCLastering(3,lambda a,b: np.sqrt(np.sum((a-b)**2)),distance_threshold =3)
c.fit(X)



