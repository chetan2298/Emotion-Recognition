#import scrip.py
from tkinter import *

#import label.py
import os

recog=Tk()
recog.title('  MINOR PROJECT ')
recog.geometry("5000x5000")
recog.configure(background='black')


Label(recog,text="SMART | HUMAN | SCANNER ",font="Helvetica 50 bold",bg='black',bd=15,fg='silver').grid(row=0,column=0, sticky=E+W+N+S)
b1=PhotoImage(file="face1.gif")
bl1=Label(recog,image=b1,bg='black')
bl1.grid(row=8,column=0,padx=5,pady=5,sticky=W+E+N+S)
Label(recog,text=" ANOUSHKA | AYUSH | CHAITANYA " ,font="Helvetica 25 bold", bg='black',bd=10, fg="silver").grid(row=4,column=0,sticky=E+W+N+S)

#Label(recog,text=" AYUSH \n ",font="Verdana 25 bold",bd=10,fg='silver').grid(row=11,column=1)
#Label(recog,text= " CHAITANYA \n",font="Verdana 25 bold",bd=10,fg='silver').grid(row=11,column=1)
#Label(recog,text=" CHAITANYA ",font="Verdana 25 bold",bd=10,fg='silver').grid(row=11,column=2)


Button(recog, text=" DETECT ", font="Verdana 15 bold" ,bd=8 ,bg='black', fg= 'white', command='func2'). grid(row=7, column=1)
Button(recog, text=" RECOGNIZE ", font="Verdana 15 bold" ,bd=5 ,bg='black', fg= 'white',command='func'). grid(row=8, column=1)
Button(recog, text=" EMOTION RECOGNIZE ", font="Verdana 15 bold" ,bd=5 ,bg='black', fg= 'white',command='do_something'). grid(row=9, column=1)


def func():
    os.startfile('Recogniser.py')
    recog.destroy()

def func2():
    os.startfile('scrip.py')
    recog.destroy()

def do_something():
    os.startfile("label.py")
    recog.destroy()


Button(recog,text='CLICK TO PROCEED',font='helv36 15 bold',bg='black',fg='silver',width=3,height=3,relief=RIDGE,command=do_something).grid(row=9,column=0,sticky=E+W)
recog.mainloop()
