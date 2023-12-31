import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
df = pd.read_csv('./sk learn/salaries.csv')

dep_var = df.drop("salary_more_then_100k", axis='columns')
ind_var = df['salary_more_then_100k'].values

le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

dep_var['company_n'] = le_company.fit_transform(dep_var['company'])
dep_var['job_n'] = le_job.fit_transform(dep_var['job'])
dep_var['degree_n'] = le_degree.fit_transform(dep_var['degree'])

x = dep_var.drop(['company','job','degree'],axis='columns')
X = x.values
model = tree.DecisionTreeClassifier()
model.fit(X , ind_var)
print(model.score(X , ind_var))
model.predict([[2,1,0]])