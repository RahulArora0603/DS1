import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
#RandomForestClassifier
df = pd.read_csv('./sk learn/HR_comma_sep.csv')
subdf = df[['promotion_last_5years','satisfaction_level','average_montly_hours','salary']]
#Creating dummy columns for Salary(high , low , medium)
salary_dummies = pd.get_dummies(df.salary, prefix="salary")
df_with_dummies = pd.concat([subdf,salary_dummies],axis='columns')
df_with_dummies.drop('salary', axis='columns', inplace=True)
x = df_with_dummies.values
y = df['left'].values
#Splitting data into training and testing
X_train , X_test , y_train , y_test = train_test_split(x, y , test_size=1/5 , random_state=0)
#Using Standard Scaler to standardize the values
scaler = StandardScaler()
x_train_data = scaler.fit_transform(X_train)
x_test_data = scaler.fit_transform(X_test)

#Creating RandomForestClassifier object
regressor = RandomForestClassifier()
regressor.fit(x_train_data ,y_train)
prediction = regressor.predict(x_test_data)
#Random prediction
pred = regressor.predict([[0 , 0.1 , 100, False, True , False]])
print(prediction)
#Accuracy of model
print(regressor.score(x_test_data, y_test)) #Output - 0.931
print(pred) #Output - [1]
