'''from PIL import Image 
from PIL import ImageFont 
from PIL import ImageDraw
import os
img = Image.open("IMG_7880[1].jpg") 
draw = ImageDraw.Draw(img) 


draw.text((50, 90), "Hello World!", (255, 255, 255)) 

img.save('sample.jpg')
file = r"IMG_7880[1].jpg"
os.chdir(r"C:\Users\pc\Desktop\Data Science")
wd = os.getcwd()
img = Image.open(file)
img.show()
'''
import turtle
turtle.color("yellow")

for i in range(5):
    turtle.forward(150)
    turtle.right(144)
    
turtle.exitonclick()