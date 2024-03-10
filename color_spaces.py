# -*- coding: utf-8 -*-
"""Homework_1_Color_Spaces.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10wQoJRyTzx_PaqrL4ximbQoymDSbHaJ6

## Installations and Requirements
"""

!pip install opencv-python
!pip install matplotlib
!pip install numpy
!pip install plotly

"""## Imports and Settings"""

import cv2
import numpy as np
import matplotlib.pyplot as plot
import plotly.graph_objects as go

import plotly.offline as pyo
pyo.init_notebook_mode(connected=True)

"""## Helper Functions"""

def plot_distribution(image):
    x = image[:, :, 0].flatten()
    y = image[:, :, 1].flatten()
    z = image[:, :, 2].flatten()
    c = image.reshape(-1, 3) / 255.0
    marker=dict(color=c, size=5)
    fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, marker=marker, mode='markers', opacity=0.3)])
    fig.show(renderer = "colab")

def plot_image(image):
    fig = go.Figure(go.Image(z=image))
    fig.show(renderer = "colab")

"""# Read Image

### Read image.jpg from the folder
"""

image_raw = cv2.imread("/content/sample_data/Images/tiger-jpg.jpg")
from google.colab.patches import cv2_imshow

"""### Theoretical question: What is unusual about OpenCV's image reading function? (hint: plot the image)"""

"OpenCV cv2.imread() function reads images in BGR format"
cv2_imshow(image_raw)

"""# Convert Image from BGR to RGB (using OpenCV)"""

image = cv2.cvtColor(image_raw,cv2.COLOR_BGR2RGB)

"""### Plot RGB Image & Distribution"""

plot_image(image)

"""## Convert Image from RGB to YUV (from scratch without using OpenCV)"""

def rgb2yuv(image):
    R = image[:,:,0]
    G = image[:,:,1]
    B = image[:,:,2]

    Y =  0.299*R + 0.587*G + 0.114*B
    U = -.16874*R -0.33126*G + 0.5*B + 128.0
    V =  0.5*R -0.41869*G - 0.08131*B +128.0

    yuv_image = np.stack((Y,U,V),axis =-1)
    return yuv_image

yuv_image = rgb2yuv(image)

"""## Plot YUV Image & Distribution"""

plot_image(yuv_image)

plot_distribution(yuv_image)

"""## Convert Image from RGB to HSV (from scratch without using OpenCV)

"""

def rgb2hsv(img):
  R = img[:,:,0]
  G = img[:,:,1]
  B = img[:,:,2]

  R = R/255.0
  G = G/255.0
  B = B/255.0

  cmax = np.max((R,G,B),axis = 0)
  cmin = np.min((R,G,B),axis = 0)
  dif= cmax - cmin + 1e-5

  h = np.zeros(cmax.shape)
  s =  np.zeros(cmax.shape)
  v = np.zeros(cmax.shape)

  key1 = cmax == cmin
  key2 = cmax == R
  key3 = cmax == G
  key4 = cmax == B
  key5 = cmax == 0
  key6 = cmax != 0

  s[key5] = 0
  s[key6] = dif[key6]/cmax[key6]
  v = cmax


  h[key1] = 0
  h[key2] = 60*(((G[key2]-B[key2])/dif[key2]))
  h[key3] = 60*(B[key3]-R[key3])/dif[key3] + 120
  h[key4] = 60*(R[key4]-G[key4])/dif[key4] + 240
  h[h<0] += 360

  hsv = np.stack([h/2, s*255, v*255], axis=-1)
  hsv[hsv>255] = 255
  return hsv

hsv_image = rgb2hsv(image)

"""## Plot HSV image & 3D distribution"""

plot_image(hsv_image)

plot_distribution(hsv_image)

"""## Shift Hue Values in HSV Color Space (from scratch without using OpenCV)"""

def shifted_h(hsv_image,shift_value):
  hsv_image[:,:,0] = (hsv_image[:,:,0] + shift_value)%180
  return hsv_image

shifted_hsv_image = shifted_h(hsv_image,300)

"""## Convert Shifted Image from HSV to RGB (from scratch without using OpenCV)"""

def hsv2rgb(hsv_image):

    h, s, v = hsv_image[:, :, 0]*2, hsv_image[:, :, 1]/255, hsv_image[:, :, 2]/255

    c = v * s
    x = c * (1 - np.abs((h / 60.0) % 2 - 1))
    m = v - c

    r, g, b = np.zeros(h.shape), np.zeros(h.shape), np.zeros(h.shape)
    key1 = (h >= 0) & (h < 60)
    key2 = (h >= 60) & (h < 120)
    key3 = (h >= 120 ) & (h < 180)
    key4 = (h >= 180) & (h < 240)
    key5 = (h >= 240) & (h < 300)
    key6 = (h >= 300) & (h < 360)

    r[key1], g[key1], b[key1] = c[key1], x[key1], 0
    r[key2], g[key2], b[key2] = x[key2], c[key2], 0
    r[key3], g[key3], b[key3] = 0, c[key3], x[key3]
    r[key4], g[key4], b[key4] = 0, x[key4], c[key4]
    r[key5], g[key5], b[key5] = x[key5], 0, c[key5]
    r[key6], g[key6], b[key6] = c[key6], 0, x[key6]

    r = (r+m)*255
    g = (g+m)*255
    b = (b+m)*255

    rgb_image = np.stack((r, g, b), axis=-1)
    return rgb_image.astype(np.uint8)

shifted_image = hsv2rgb(shifted_hsv_image)

plot_image(shifted_image)

plot_distribution(shifted_image)