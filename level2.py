import json
import requests
r = requests.get("http://ankursingh.xyz/api/productshow.php")
#print(type(r))
#print(r)
data = r.json().values()
datalist =[]
for i in data:
    datalist.append(i)
dictdata = datalist[0][0]
print(dictdata['product_id'])
  


