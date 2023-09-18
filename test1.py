import pandas as pd
import csv
df = pd.read_csv('data1.csv')
#df.to_csv(index=1, )
#print(type(df))
rowList = []
for index, rows in df.iterrows():
    mylist = [rows['Account'] , rows['User'] , rows['AccNo']]
    rowList.append(mylist)
print(rowList)
   