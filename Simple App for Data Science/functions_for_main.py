import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler 
#import csv
df = pd.read_csv('./sk learn/HR_comma_sep.csv')
#df.to_csv(index=1, )
#print(type(df))
def MultiColInput():
   colnames = input("Enter columns seperated by comma : ")
   mylist = colnames.split(',')
   print(df[mylist])

def checkDataType(val):
   cols = val.head(0)
   headlist = []
   for i in cols:
      if str(val[i].dtype).startswith("int")==True or str(val[i].dtype).startswith("float")==True :
        headlist.append(i)
   print(headlist)

def MyBarGraph(val):
    category = input("Enter categorical heading : ")
    x = val[category].value_counts().index
    y = val[category].value_counts().values
    print(x)
    plt.bar(x, y)
    plt.show()

def myPieChart(val):
    category = input("Enter categorical heading : ")
    x = val[category].value_counts().index
    y = val[category].value_counts().values
    plt.pie(y , labels=x)
    plt.show()


def MachLearn(mydf):
   print("Choose the Machine Learning model based on Data :\n[I recommend checking if the data is linear using Graphs]\n")
   modtype = input("Press 'D' for Linear Regression , 'E' for Logistic Regression, 'F' to return to main menu : ")
   if modtype=='D':
      para1 = input("Enter independent variables : ")
      para2 = input("Enter dependent variables : ")
      comma = ','
      if comma in list(para1):
         para1 = para1.split(',')
         x = mydf[para1].values
         y = mydf[para2].values
      else:
         x = mydf[para1].values
         y = mydf[para2].values
         x = x.reshape(-1 , 1)
      X_train , X_test , Y_train , Y_test = train_test_split(x , y , test_size=1/4 , random_state=0)  
      model = LinearRegression()
      model.fit(X_train, Y_train)
      ypred = model.predict(X_test)
      print(ypred)
      to_predict = input("Enter values to predict: ")
      if comma in list(to_predict):
        to_predict=to_predict.split(",")
        ipredict = []
        for i in range(0, len(para1)):
           if str(mydf[para1[i]].dtype).startswith("int")==True:
               r = int(to_predict[i])
               ipredict.append(r)
           elif str(mydf[para1[i]].dtype).startswith("float")==True:
               r = float(to_predict[i])
               ipredict.append(r)
        print(ipredict)         
        prediction = model.predict([ipredict])
        print(prediction)   
      else:
        mypred = int(to_predict)
        prediction = model.predict([[mypred]])
        print(prediction)      
   elif modtype=='E':    
      para1 = input("Enter independent variables : ")
      para2 = input("Enter dependent variables : ")
      comma = ','
      if comma in list(para1):
         para1 = para1.split(',')
         x = mydf[para1].values
         y = mydf[para2].values
      else:
         x = mydf[para1].values
         y = mydf[para2].values
         x = x.reshape(-1 , 1)
      X_train , X_test , Y_train , Y_test = train_test_split(x , y , test_size=1/4 , random_state=0)  
      model = LogisticRegression()
      model.fit(X_train, Y_train)
      ypred = model.predict(X_test)
      print(ypred)
      to_predict = input("Enter values to predict: ")
      if comma in list(to_predict):
        to_predict=to_predict.split(",")
        ipredict = []
        for i in range(0, len(para1)):
           if str(mydf[para1[i]].dtype).startswith("int")==True:
               r = int(to_predict[i])
               ipredict.append(r)
           elif str(mydf[para1[i]].dtype).startswith("float")==True:
               r = float(to_predict[i])
               ipredict.append(r)
        print(ipredict)         
        prediction = model.predict([ipredict])
        print(prediction)   
      else:
        mypred = int(to_predict)
        prediction = model.predict([[mypred]])
        print(prediction)