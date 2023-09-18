import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('car.csv')
df1 = df.head(9)
cricketdf = pd.read_csv('./Batting/t20.csv')
#GROUP BY MULTIPLE COLUMNS - 
#df1 = df.head(9)
data = df1.groupby(['Drivetrain','Body Type'])
for name,group in data:
    print(name)
    print(group)
'''USING ILOC function -
print(df[['Company','Model', 'Horsepower' ]].iloc[1:4])
print(df.iloc[2,0])'''
'''PREVIOUS PROJECT DONE IN 3 LINES-
for index,rows in df.iterrows():
    if rows['Company']=="Toyota":
        print(rows[['Company','Model', 'Horsepower']])'''
'''READING A TXT FILE WITH read_csv-
   df = pd.reas_csv('data.txt', delimiter="\t")'''
'''DESCRIBING DATA-
print(df.describe())'''
'''SORTING IN DESCENDING ORDER-
print(df1.sort_values(['Company','Body Type'], ascending=False))'''
'''FAILED NUMERIC OPERATIONS -

cricketdf['50 Plus'] = cricketdf['100']+cricketdf['50']
print(cricketdf['50 Plus'])
print(cricketdf['Runs'].sum())'''
#print(data['Number of Doors'].sum())
pricelist = []
price = list(df1['Price'])
print(price)
for pri in price:

   p = pri.split("$")[1].split(",")[1]
   q = pri.split("$")[1].split(",")[0]
   r = q+p
   #print(r)
   p1 = int(r)
   pricelist.append(r)
print(pricelist)   


#for p in price:
#   pricelist.append(int(p))
#print(pricelist)   

    #datalist.append(group['Horsepower'])
#print(datalist)


