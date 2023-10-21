'''import random

list1 = []
list2 = []

def player1():
    start = input("Player1 : Press S to play your luck\n")
    if start=="S":
       randomnum = random.randint(1,6)
       print(randomnum)
       list1.append(randomnum)
    else:
        print("Press S only , no other input allowed.")
        player1()   
def player2():
    start1 = input("Player2 : Press S to play your luck\n")
    if start1=="S":
       rnum = random.randint(1,6)
       print(rnum)
       list2.append(rnum)
    else:
        print("Press S only , no other input allowed.")
        player2() 

def Comp():
    rnum = random.randint(1,6)
    print(f"Comp : {rnum}")
    list2.append(rnum)
def mainfunc():
    amtofplayers = input("Press A for 2 player, B for Computer : ")
    if amtofplayers=="A":
       for i in range(20,40):
          if i%2==0:
              player1()
          else:
              player2()
    elif amtofplayers=='B':
       for i in range(20,40):
          if i%2==0:
              player1()
          else:
              Comp() 
    print(list1)
    print(list2)        
    sum1 = sum(list1)
    sum2 = sum(list2)
    if sum1>sum2:
        print("Player1 wins")
    elif sum2>sum1:
        print("Computer wins")

mainfunc()'''
from tkinter import *

#def click():
#    pass
root = Tk()
frame = Frame(root, height= "800" ,width="800")
frame.pack()
btn = Button(frame, text="Enter")
btn.pack()
ent = Entry(frame, bg="white")
ent.pack()
if btn.invoke()==True:
    ent.insert(0, "Ten")

root.mainloop()