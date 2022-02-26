#!/usr/bin/env python3

import sys
from  tkinter import *
#import time 

from datetime import datetime


def times():
	curr_time = datetime.now()
	formatted_time = curr_time.strftime('%H:%M:%S.%f')
	#current_time=time.strftime("%H:%M:%S.%f") 
	clock.config(text=formatted_time[0:12])
	clock.after(200,times)


root=Tk()
root.geometry("500x250")
clock=Label(root,font=("times",50,"bold"),bg="black",fg='blue')
clock.grid(row=2,column=2,pady=25,padx=100)
times()

digi=Label(root,text="Digital clock",font="times 24 bold",fg="violet")
digi.grid(row=0,column=2)

nota=Label(root,text="hours   minutes   seconds   ",font="times 15 bold")
nota.grid(row=3,column=2)

root.mainloop()

