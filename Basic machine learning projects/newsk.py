import numpy as nm  
import matplotlib.pyplot as plt 
import pandas as pd  
from sklearn.linear_model import LogisticRegression  
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

data_set= pd.read_csv('./sk learn/suv_data.csv')  

x= data_set.iloc[:, [2,3]].values  
y= data_set.iloc[:, 4].values
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

st_x= StandardScaler()    
x_train= st_x.fit_transform(X_train)    
x_test= st_x.transform(X_test)
classifier= LogisticRegression(random_state=0)  
classifier.fit(x_train, y_train)
'''C=1.0, class_weight=None, dual=False, fit_intercept=True,  
                   intercept_scaling=1, l1_ratio=None, max_iter=100,  
                   multi_class='warn', n_jobs=None, penalty='l2',  
                   random_state=0, solver='warn', tol=0.0001, verbose=0,  
                   warm_start=False)'''
y_pred= classifier.predict(x_test)
cm= confusion_matrix(y_test, y_pred)
print(cm)
print("Accuracy: ",accuracy_score(y_test, y_pred))