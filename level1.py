import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('car.csv')
#print(df['Price'])
pricelist = []
df1 = list(df['Price'])
for p in df1:
    r = list(p)
    if r[0]=="$" and len(r)<=8 :
        n = p.split("$")[1].split(",")[1]
        m = p.split("$")[1].split(",")[0]
        i = m+n
        #print(r)
        p1 = int(i)
        pricelist.append(i)
    elif r[0]=="R":
        sp1 = p.split(" - ")[0].split(". ")[1]
        sp2 = p.split(" - ")[1].split(" ")[0]
        fl1 = float(sp1)
        fl2 = float(sp2)
        i2 = (fl1 + fl2)/2
        pricelist.append(i2)
    elif r[0]=="$" and len(r)>8:
        spl1 = p.split("-")[]    

