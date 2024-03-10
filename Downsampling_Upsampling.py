# -*- coding: utf-8 -*-
"""Homework_2(pixeria).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mQiSAD-ypNMLdDU0As2Y4thcXPSWL9F9
"""

import numpy as np
import cv2
from google.colab.patches import cv2_imshow

cd/content/sample_data/Image/

image_raw = cv2.imread('face.webp')

downsampled_image = cv2.resize(image_raw,(0,0),fx = 0.5, fy =0.5,interpolation= cv2.INTER_LINEAR)
downsampled_image =  cv2.resize(downsampled_image,(0,0),fx = 0.5, fy =0.5,interpolation= cv2.INTER_LINEAR)
cv2_imshow(image_raw)
cv2_imshow(downsampled_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

inter_nearest = cv2.resize(downsampled_image,(0,0),fx = 4,fy = 4,interpolation= cv2.INTER_NEAREST)
inter_area = cv2.resize(downsampled_image,(0,0),fx = 4,fy = 4, interpolation = cv2.INTER_AREA)
inter_cubic = cv2.resize(downsampled_image,(0,0),fx = 4,fy = 4, interpolation =cv2.INTER_CUBIC)
inter_lanczos4 = cv2.resize(downsampled_image,(0,0),fx = 4,fy = 4,interpolation= cv2.INTER_LANCZOS4)

stack = np.hstack((inter_nearest,inter_area,inter_cubic,inter_lanczos4,image_raw[0:432,:,:]))

cv2_imshow(stack)

cv2_imshow(inter_nearest)
cv2_imshow(inter_area)
cv2_imshow(inter_cubic)
cv2_imshow(inter_lanczos4)

cv2.waitKey(0)
cv2.destroyAllWindows()