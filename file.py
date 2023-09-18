import csv
import pandas as pd
#accList =[]

def Account():
   accName = input("Enter account Name: ")
   accNo = input("Enter account No. : ")
   file1 = open("check.csv","r")
   checklist = file1.readline()
   file1.close()
   if accNo in checklist:
         print("Enter Valid Number")
         Account()
   else:
      mylist = ["Account", f"{accName}", f"{accNo}"]
      with open('data.csv',"a") as file:
         csvwriter = csv.writer(file)
         csvwriter.writerow(mylist)
         file.close()
      file1 = open("check.csv", "a")
      file1.write(f"{accNo}")
      file1.close()
#     accList.append(accNo)
#     print(accList)
      Program()

def Deposit():
   accNo = input("Enter account No. : ")
   file1 = open('check.csv', "r")
   checklist = file1.readline()
   file1.close()
   if accNo in checklist:
     depositAmt = input("Enter amount:")
     df = pd.read_csv('data.csv')
     df.loc[int(accNo)-0.5] = ["Deposit", f"{accNo}",f"{depositAmt}"]
     df1 = df.sort_index().reset_index(drop=True)
     print(df1)
     with open('data.csv',"w") as file:
         file.write(df1.to_string())
     #rowList = []
     #for index, rows in df.iterrows():
     #   mylist = [rows['Account'] , rows['User'] , rows['AccNo']]
     #   rowList.append(mylist)
     #print(rowList)   
     Program()
   elif accNo=='S':
     print("You are out of the loop")
   else:
     print("Enter Valid Account Number")
     Deposit()

def Withdraw():
   accNo = input("Enter account No. : ")
   file1 = open("check.csv","r")
   checklist = file1.readlines()
   file1.close()
   if accNo in checklist:
      withAmt = input("Enter amount:")
      file = open("data.csv","a")
      file.write(f"Withdraw\t{accNo}\t{withAmt}\n")
      file.close()
      Program()
   elif accNo=='S':
      print("You are out of the loop")
   else:
      print("Enter Valid Account Number")
      Withdraw()   

def Program():
   print("To Create a account type 'A' , To Deposit type 'D', To withdraw type 'W'")
   action = input("TYPE HERE: ")
   if action=='A':
      Account()
   elif action=='D':
      Deposit()
   elif action=='W':
      Withdraw()
   else:
      print("Enter 'A'or'D'or'W'!")   

Program()