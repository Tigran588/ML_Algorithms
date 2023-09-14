# -*- coding: utf-8 -*-
"""mnist_NN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OCfG9yovI_BQrkV_30Qm8_uXg4uRuV9t
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import mnist

(x_train,y_train),(x_test,y_test) = mnist.load_data()

x_train = x_train/255
x_test = x_test/255\

y_test = to_categorical(y_test,10)
y_train = to_categorical(y_train,10)

input = keras.Input((28,28,1),name = 'mnist')
x = layers.Conv2D(32,3,activation = 'relu')(input)
x = layers.Conv2D(64,3,activation = 'relu')(x)
x = layers.MaxPooling2D(3)(x)
x = layers.Conv2D(64,3,activation = 'relu',padding = 'same')(x)
x = layers.Conv2D(64,3,activation = 'relu',padding = 'same')(x)
x = layers.MaxPooling2D(3)(x)
x = layers.Flatten()(x)
x = layers.Dense(64)(x)
output = layers.Dense(10,activation = 'softmax')(x)

model = keras.Model(input,output)

model.compile(optimizer = 'adam',loss = 'categorical_crossentropy',metrics = ['accuracy'] )

#callback = [keras.callbacks.EarlyStopping(monitor = 'loss',min_delta = 0.01,verbose = 1)]
model.fit(x_train,y_train,batch_size = 70,epochs = 5,validation_data = (x_test,y_test))

model.evaluate(x_test,y_test)