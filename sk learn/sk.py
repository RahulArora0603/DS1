import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
df = pd.read_csv('Salary_Data.csv')
#df1 = df['YearsExperience']
#df2 = df['Salary']
x = df.iloc[1:, :-1].values
y = df.iloc[1:, 1:].values

X_train , X_test , y_train , y_test = train_test_split(x, y , test_size=1/3 , random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

rinter = regressor.intercept_
rco = regressor.coef_
y_pred1  = rinter + rco*X_test
print(y_pred1)

y_pred = regressor.predict(X_test)
regressor.score(X_test, y_test)
print(y_pred)
plt.scatter(X_train , y_train, color = "red")
plt.plot(X_train, regressor.predict(X_train), color="blue")
plt.title('Salary vs Experience(Training set)')
plt.xlabel('Years of EXPERIENCE')
plt.ylabel('Salary')
plt.show()
plt.scatter(X_test , y_test, color = "green")
plt.plot(X_train, regressor.predict(X_train), color="blue")
plt.title('Salary vs Experience(Test set)')
plt.xlabel('Years of EXPERIENCE')
plt.ylabel('Salary')
plt.show()