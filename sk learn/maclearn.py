import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
#Linear Regression (MULTIPLE VARIABLE)
'''df = pd.read_csv('bmi.csv')
df1 = df.drop('BmiClass', axis='columns')
#print(df1)
x = df1.drop('Bmi', axis='columns').values
y = df1['Bmi'].values

X_train , X_test , y_train , y_test = train_test_split(x, y , test_size=1/3 , random_state=0)

regressor = LinearRegression()
regressor.fit(x, y)
y_pred = regressor.predict([[60,1.70,72]])
#regressor.score(X_test, y_test)
print(y_pred)
print(regressor.coef_)'''
df = pd.read_csv('./sk learn/HR_comma_sep.csv')
'''SALARY AND LEFT GRAPH-
pd.crosstab(df.salary,df.left).plot(kind='bar')
plt.show()'''
subdf = df[['promotion_last_5years','satisfaction_level','average_montly_hours','salary']]
salary_dummies = pd.get_dummies(df.salary, prefix="salary")
df_with_dummies = pd.concat([subdf,salary_dummies],axis='columns')
df_with_dummies.drop('salary', axis='columns', inplace=True)
x = df_with_dummies.values
#print(df_with_dummies.head())
#print(x)
y = df['left'].values
X_train , X_test , y_train , y_test = train_test_split(x, y , test_size=1/5 , random_state=0)
regressor = LogisticRegression()
regressor.fit(X_train ,y_train)

pred = regressor.predict([[0 , 0.1 , 100, False, True , False]])
#print(regressor.score(X_test, y_test))
print(pred)
