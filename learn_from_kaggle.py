import pandas as pd


df = pd.read_csv('./sk learn/salaries.csv')

r = df.groupby('company')[['company','job']]
pairs = dict()
for j in r.groups:
    pairs[j] = df['job'].iloc[r.groups[j]].to_numpy()

print(pairs['facebook'])