'''import cv2
img = cv2.imread('screenshot1.png') 
cv2.imshow('image', img) 
cv2.waitKey(0)       
cv2.destroyAllWindows()'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('IMG_7880[1].jpg')

'''GRAYSCALE
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

fig, ax = plt.subplots(1, 2, figsize=(8, 4))


ax[0].imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
ax[0].set_title("Original")

ax[1].imshow(cv.cvtColor(gray_image, cv.COLOR_BGR2RGB))
ax[1].set_title("Grayscale")
plt.show()'''
'''CIRCLE
cv.circle(img=img, center = (70,40), radius =35, color =(255,0,0), thickness=1)'''
'''RECTANGLE
cv.rectangle(img, pt1=(40,10), pt2=(100,70), color=(255,0,0), thickness=1)'''

'''new_img = cv.resize(img , (300,200))
cv.imshow('image',new_img)'''
cv.waitKey(0)
#plt.show()