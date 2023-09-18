import pandas as pd
#df = pd.read_csv('./Batting/t20.csv')
#print(df.describe())
import matplotlib.pyplot as plt
def Line(abc):
   plt.plot(abc)
   plt.show()  

def Bar(x,y):
   plt.bar(x , y)
   plt.show()

def Graph(abc1, abc2):
  number = int(input("Type 1 for Bar Graph , 2 for Line graph, 3 for break: \n"))
  if number==1:
     Bar(abc1,abc2)
  if number==2:
     Line(abc1)  

def Data(name):
  print(name)
   

while True:
   df = pd.read_csv('./Batting/t20.csv')
   print(df.head(0))

   data1  = input("Enter heading 1: ")
   data2  = input("Enter heading 2: ")
   df0 = df.head(10)
   df1 = df0[data1]
   df2 = df0[data2]
   num = int(input("enter 1 for graph\n 2 for data \n 3 for break\n"))

   #df2 = list(df1)
   

   if num==1:
      Graph(df1 , df2)
   elif num==2:
      Data(df1)
   elif num==3:
      break
   else:
      print("enter right input")      



