import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

df = pd.read_csv('./sk learn/co2data.csv')
#df1 = df.loc[df['Car']=="Ford"]
#print(df1)
df1 = pd.get_dummies(df['Car'], prefix='Car')
df2 = pd.concat([df, df1], axis='columns')
df2.drop(['Car','Model','CO2'], axis='columns', inplace=True)
#print(df2)
x = df2[1:].values#df[['Volume', 'Weight']].iloc[1:].values
y = df['CO2'].iloc[1:].values
Xtrain , Xtest ,Ytrain , Ytest = train_test_split(x , y , test_size=1/5 , random_state=0)
regresor = LinearRegression()
regresor.fit(Xtrain, Ytrain)
pred = regresor.predict(Xtest)
print(pred)
print(regresor.score(Xtest, Ytest))
print(Xtest)
#plt.scatter(df1['CO2'] ,df1['Volume'], color="red")
#plt.show()'''