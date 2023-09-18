import pandas as pd
import matplotlib.pyplot as plt

df =pd.read_csv('./Batting/t20.csv')
print(df)
player = df['Player']
print(player)
#clst =[]
#for p in player:
#   print(p)
#   clst.append(p.split("(")[1].split(")")[0])
#print(set(clst))
#cntryname = input("Enter country name[Capital letters]: ")
#indiann=[]
#for index , rows in df.iterrows():
##    if rows.Player.split("(")[1].split(")")[0] ==cntryname:
##        indiann.append(list(rows))
#     hundred = [rows.Player , rows['50']]
#     indiann.append(hundred)
#print(indiann,end="")
#name=[]
#fifty =[]
#for data in indiann:
#    print(type(data[1]))
#    if data[1]!="0" or data[1]!="-":
#      #print(data[1])
#      name.append(data[0])
#      fifty.append(data[1])
#print(name)
#print(fifty)
#plt.plot([7,9],[8,10])
#plt.show()
#print("********************************")
    #print(rows.Player,end="")


#indialst=[]
#for c in clst:
    #if(c=="INDIA"):
     #   indialst.append(df)
#SSprint(indialst)

#V Kohli (INDIA)


# df =pd.read_csv('cardata.csv')
# print(df)
# print("******************************")

#print(df.head(0))
#print(df.head())
#print("******************************")
#print(df.tail(1))
#print("******************************")
#print(df.columns)
#print(df.shape)
#print(df["Car_Name"])


# read list
""" 
df = pd.DataFrame([4,3,5,6,7])
print(df)

data = [["user1","user2","user3"],[4,5,6],[300,500,600]]
df  =pd.DataFrame(data)
print(df)



print("****************************")
data = [
        ["name","age","salary"],
        ["user1",30,4000],
        ["user2",40,5000],
        ["user3",20,3000],
        ["user4",45,6000],
    ]
df  =pd.DataFrame(data)
print(df)


print("****************************")
col =["name","age","salary"]

data = [
        ["user1",30,4000],
        ["user2",40,5000],
        ["user3",20,3000],
        ["user4",45,6000],
    ]
df  =pd.DataFrame(data,columns=col)
print(df)

print("****************************")
col =["name","age","salary"]
row = ["100","200","300","400"]
data = [
        ["user1",30,4000],
        ["user2",40,5000],
        ["user3",20,3000],
        ["user4",45,6000],
    ]
df  =pd.DataFrame(data,columns=col,index=row)
print(df)


print("****************************")
col =["name","age","salary"]
row = ["R1","R2","R3","R4"]
data = [
        ["user1",30,4000],
        ["user2",40,5000],
        ["user3",20,3000],
        ["user4",45,6000],
    ]
df  =pd.DataFrame(data,columns=col,index=row)
print(df)
 """

""" #dict data

data ={
    "id":[1,2,3,4,5],
    "name":["user1","user2","user3","user4","user5"],
    "salary":[200,300,400,500,600]
}


df = pd.DataFrame(data)
print(df)
print(df[['name',"salary"]])
 """

#data =[
#        {"user1",30,400},
#        {"user2",50,700},
#        {"user3",34,450},
#        {"user4",20,500},
#    ]
#
#df = pd.DataFrame(data)
##df = pd.read_json(data)
#print(df)


""" data = {
   "user":[ {"firstName":"John", "lastName":"Doe"},
{"firstName":"Anna", "lastName":"Smith"},
{"firstName":"Peter", "lastName":"Jones"}
   ]
}

df =pd.DataFrame(data)
print(df) """