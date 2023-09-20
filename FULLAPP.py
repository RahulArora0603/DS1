import pandas as pd
df = pd.read_csv('t20.csv')
print(df.head(0))
df1 = df.head(50)
inputdata = input("Enter 'A' for All Data , 'P' for Player Details , 'D' for Grouped Data , 'T' for Total\n")
if inputdata=='A'or inputdata=='a':
    print(df1)
elif inputdata=='P' or inputdata=='p':
    print(df1['Player'])
    playlist = []
    for i in df1['Player']:
        k = i.split(" (")[0]
        r = k 
        playlist.append(r)
    #print(playlist)
    df1.insert(2 , 'Name', playlist)
    name = input("Enter player name: ")

    print(df1.loc[df1['Name']==name])
elif inputdata=='D'or inputdata=='d':
    print(df1.head(0))
    heading = input("Group according to: ")
    df2 = df1.groupby(heading)
    for data , group in df2:
        print(data)
        print(group)
elif inputdata=='T'or inputdata=='t':
    print(df.head(0))
    header = input("Enter the heading: ")
    dlist = []
    mlist = list(df1[header])
    for i in mlist:
        j = list(i)
        if i!="-" and j[-1]!="*":
          g = int(i)
          dlist.append(g)
        elif j[-1]=="*":
          item = int(i.split("*")[0])
          dlist.append(item) 
    print(f"Total: {sum(dlist)}")
