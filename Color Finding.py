from tkinter import *
import random

from tkinter import messagebox

screen = Tk()
screen.geometry("600x600")
screen.title("Color game")


timeleft=30

def start(event):
    t2.config(text="")
    if timeleft==30:
        countdown()
        
    nextcolor()

def nextcolor():
    global s
    global timeleft

    if timeleft > 0:
        i.focus_set()
        if i.get().lower()==colors[1].lower():
            s+=1

        i.delete(0,END)
        random.shuffle(colors)
        t3.config(fg = str(colors[1]),text = str(colors[0]))
        score = Label(text = "SCORE : " + str(s),font =('Arial',15),fg = 'red')
        score.place(x=220,y=90)

    if timeleft == 0:
        messagebox.showinfo(" game over ",f'hey time is up and your score is {s}')

def countdown():
    global timeleft

    if timeleft > 0:
        timeleft-=1
        tm=Label(screen,text = 'Time Left :' + str(timeleft),font = ('Arial',15),fg = 'red')
        tm.after(1000,countdown)

colors = ['Red','Blue',"Orange",'yellow','pink','purple','brown','white']
s=0

t=Label(screen,text='Remember ! Please type the color name not the word text ',font = ('Arial',17),fg= 'Green')
t.place(x=10,y=30)

t2 = Label(screen,text = "PRESS ENTER TO START",font = ('Aria',17),fg = 'Red')
t2.place(x= 180,y = 180)

t3 = Label(screen,text = (),font = ('Arial',45),fg = 'Red')
t3.place(x= 180,y = 180)

t4 = Label(screen,text = "Time = 30 seconds",font = ('Aria',17),fg = 'Red')
t4.place(x= 180,y = 150)

i = Entry(screen,font=('Aria',18),fg = 'black',width = 15)
i.place(x=200 , y= 400)

screen.bind('<Return>',start)
i.focus_set()


screen.mainloop()