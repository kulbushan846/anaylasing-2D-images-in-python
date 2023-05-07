"""
analysing 2D images

"""
from skimage import io
img = io.imread('om.jpg') #read image
#io.imshow(img) # show image

import matplotlib.pyplot as plt
#plt.imshow(img) 
#img_gray = io.imread('om.jpg', as_gray=True) # read imaga as gary color image
#plt.imshow(img_gray,cmap="hot")  #change color
#plt.imshow(img_gray,cmap="jet")  # change color

"""
fig = plt. figure(figsize = (10,10))
ax1 = fig.add_subplot(2,2,1)
ax1 = plt.imshow(img_gray, cmap='hot')

ax2 = fig.add_subplot(2,2,2)
ax2 = plt.imshow(img_gray, cmap='jet') 

ax3 = fig.add_subplot(2,2,3)
ax3 = plt.imshow(img_gray, cmap= 'copper') 
"""
import cv2
gray_img = cv2.imread('om.jpg',0)
color_img = cv2.imread('om.jpg',1)



#cv2.imshow("pic frrm skimage", img)
#cv2.imshow("gray image frrm cv2", gray_img)
#cv2.imshow("color image from cv2", color_img)


fig = plt. figure(figsize = (10,10))
ax1 = fig.add_subplot(2,2,1)
ax1 = plt.imshow(img)

ax2 = fig.add_subplot(2,2,2)
ax2 = plt.imshow(gray_img) 

ax3 = fig.add_subplot(2,2,3)
ax3 = plt.imshow(color_img) 

ax4 = fig.add_subplot(2,2,4)
ax4 = plt.imshow(img, cmap='flag') 