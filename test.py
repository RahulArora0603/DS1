import pandas as pd
#df = pd.read_csv('./Batting/t20.csv')
#print(df.describe())
import os
import matplotlib.pyplot as plt
'''OS Library functions-
data=os.listdir(os.getcwd())
print(data)
name =input("enter file name")
df = pd.read_csv(os.getcwd()+"/"+name)
print(df)
'''
import cv2
'''#CV2 Images-
image = cv2.imread('screenshot1.png')
h, w = image.shape[:2]
(B,G,R)= image[100, 100]
#print(f"Red ={R}, Green={G},Blue={B}")
cv2.imshow("Display window", image)
k = cv2.waitKey(0)
#Resizing -
newimg = cv2.resize(image,(600,500))'''
#print(cv2.__file__)
'''video_cap = cv2.VideoCapture(0)
ret , video_data = video_cap.read()
cv2.imshow()
'''
