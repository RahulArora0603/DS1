import pandas as pd
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
digits = load_digits()
#print(digits.data[0])

'''plt.gray()
for i in range(4):
    plt.matshow(digits.images[i])
    plt.show()'''

df = pd.DataFrame(digits.data)
df['target'] =  digits.target
x = df.drop('target', axis='columns')
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
model = RandomForestClassifier(n_estimators=50 , criterion='gini')
model.fit(X_train, y_train)
print(model.score(X_test,y_test))