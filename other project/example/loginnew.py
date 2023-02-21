from cProfile import label
from email.mime import image
#from logging import root
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import *
from time import strftime
from tkinter.ttk import Style
from turtle import width
from setuptools import Command
import os
from subprocess import call
from PIL import ImageTk, Image  
import pyodbc  

def Ok():
	conn = pyodbc.connect('Driver={SQL Server};'
					  'Server=DESKTOP-LEGECK4;'
					  'Database=test;'
					  'Trusted_Connection=yes;')
	mycursor = conn.cursor()
	mycursor.execute("select * from users where bname=? and password=?",(userinput.get(),passinput.get()))
	results = mycursor.fetchall()
	
	
	if results:
		#tk.messagebox.showinfo("","Login Success")
		call(["python", "call files/new.py"])
		return True
	else:
		#tk.messagebox.showinfo("","Login incorrect password")
		Label(root, text="Please enter a correct username and password",font=("Goudy old style",15,"bold"),fg='red',bg='#95baa8').place(x=480, y=530)
		return False

root = Tk()
root.title("Login")

root.geometry("{0}x{0}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(bg='#384a5d')
color_me = Label(root, text='(217, 217, 217) #d9d9d9',font = ('Times', 20),relief = SOLID,padx=20, pady=20)
color_me = Label(root, text='(217, 217, 217) #d9d9d9',font = ('Times', 20),relief = SOLID,padx=20, pady=20)

rot_i = Image.open("")
rotunda = ImageTk.PhotoImage(rot_i)
label2 = tk.Label(image=rotunda,bg='#384e5d')
label2.image = rotunda
label2.place(x=430,y=255)

frame_login=Frame(root, bg='#95baa8', highlightbackground="black", highlightthickness=2).place(height=40,width=1400,x=0,y=0)
root.attributes('-fullscreen',True)

user_input=tk.StringVar()
pass_input=tk.StringVar()
userinput = tk.Entry(root, bootstyle="danger",textvariable=user_input,bg='light grey',font=15)

userinput.place(x=600, y=323,height=22,width=280)
passinput = Entry(root, textvariable=pass_input,bg='light grey',font=15)
passinput.place(x=600, y=352,height=22,width=280)
passinput.config(show="*")
Label(root, text="Username",font=("Goudy old style",13,"bold"),fg='black',bg='#384e5d').place(x=500, y=323)
Label(root, text="Password",font=("Goudy old style",13,"bold"),fg='black',bg='#384e5d').place(x=500, y=350)

exit_button = Button(root,text='Cancel',command=lambda: root.quit(),bd=2,bg="grey",fg="red",highlightcolor="purple",activeforeground="green",activebackground="grey",  relief="groove",width = 9,height =9,font=("times new roman",12),accelerator= "Ctrl+Q").place(x=750, y=400)
login_button = Button(root,  text="Login", command= lambda:[Ok()],bd=2,bg="grey",fg="red",  relief="ridge",width = 9,height =1,font=("times new roman",12,"bold")).place(x=600, y=400)
#-------------------Label Time----------------
#Define a callback function for exit


def my_time():
    time_string = strftime('%H:%M:%S %p') # time format 
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds 
my_font=('times',14,'bold') # display size and style
l1=tk.Label(root,font=my_font,bg='#95baa8')
l1.grid(row=0,column=1,padx=5,pady=5)
my_time()
#-------------------Label Time----------------
# default date entry
ttk.DateEntry()
# success colored date entry
bb1=ttk.DateEntry(bootstyle="readonly")
bb1.pack(side=LEFT, padx=10, pady=10)
root.mainloop()




