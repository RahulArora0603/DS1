import pandas as pd

df = pd.read_csv('./Batting/t20.csv')
#print(df)

row_list = []
for index , rows in df.iterrows():
    row_list.append(rows)

headlist = df.head(0)
#print(row_list)
#file = open("indplayer.csv","w")
#file.write()#f"{headlist[0]}\t{headlist[1]}\t{headlist[2]}\t{headlist[3]}\t{headlist[4]}\t{headlist[5]}\t{headlist[6]}\t{headlist[7]}\t{headlist[8]}\t{headlist[9]}\t{headlist[10]}\t{headlist[11]}\t{headlist[12]}\t{headlist[13]}\t{headlist[14]}\n"
#file.close()
for prow in row_list:
    if prow[1].split("(")[1].split(")")[0]=="INDIA":
        print(f"{prow}\n")
        file = open("indplayer.csv","a")
        file.write(f"\n{prow}")
        file.close()

#alldata = []
#
#for data in df:
#    alldata.append(data)
#
#print(alldata)
    

#player = df['Player']
#print(player)
#cntrylist =[]
#for p in player:
#    cntrylist.append(p.split("(")[1].split(")")[0])
#
#print(cntrylist)    
#indList =[]
#for cntry in cntrylist:
#    if cntry=="INDIA":
#        indList.append()
#
#print(indList)