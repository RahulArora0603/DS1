import random
from tkinter import *
#from tkinter import Tk
list1 = []
list2 = []

def player1():
   
    randomnum = random.randint(1,6)
    player1_text.delete(0, END)
    player1_text.insert(0,randomnum)
    list1.append(randomnum)   
def player2():
    player2_button['state']='normal'
    #player1_button['state']='disabled'
    rnum = random.randint(1,6)
    player2_text.delete(0, END)
    player2_text.insert(0,rnum)
    list2.append(rnum)
'''def turn1():
    player1_button['state']='normal'
    player2_button['state']='disabled'   

def turn2():
    player2_button['state']='normal'
    player1_button['state']='disabled'   
'''
def start():
    player1_button['state']='normal'
    player2_button['state']='normal'
    player1_text.delete(0, END)
    player2_text.delete(0, END)
    total_label.delete(0,END)
    list1.clear()
    list2.clear()
    start_button.config(text="Stop")
    start_button.config(command=pause)

def pause():
    player1_button['state']='disabled'
    player2_button['state']='disabled'
    start_button.config(text="Start")

    start_button.config(command=start)

def resume():
    player1_button['state']='disabled'
    player2_button['state']='disabled'
    

def result():
   sum1 = sum(list1)
   sum2 = sum(list2)
   total_label.insert(0, f"Player1 : {sum1} | Player2 : {sum2}")

   if sum1>sum2:
       #total_label.delete(0, END)
       total_label.insert(0,"\nPlayer 1 Wins")
   elif sum2>sum1:
       #total_label.delete(0, END)
       total_label.insert(0,"\nPlayer 2 Wins")     
#mainfunc()
root = Tk()
frame = Frame(root, height= "800" ,width="800")
frame.pack()
game_name_label = Label(frame, text="Luck Game").pack()
player1_button = Button(frame, text="Player 1", command= player1, state=DISABLED)

player1_button.pack()
player1_text = Entry(frame, bg="white",width="6")
player1_text.pack()

player2_button = Button(frame, text="Player 2", command=player2, state=DISABLED)
player2_button.pack()
player2_text = Entry(frame, bg="white", width="6")
player2_text.pack()
total_label = Entry(frame, bg="white", width="50")
total_label.pack()
resume_btn = Button(frame , text="Resume", command=resume)
start_button = Button(frame, text="Start", command=start)
start_button.pack()
result_btn = Button(frame, text="Result", command=result)            
result_btn.pack()

root.mainloop()
