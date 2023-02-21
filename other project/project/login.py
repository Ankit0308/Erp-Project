from cProfile import label
from email.mime import image
from logging import root
import tkinter as tk
from tkinter import *
from time import strftime
from tkinter.ttk import Style
from turtle import width
from unittest import result
from pkg_resources import ResolutionError
from setuptools import Command
import os
from subprocess import call
from PIL import ImageTk, Image  
import pyodbc  

def Ok():
	conn = pyodbc.connect('Driver={SQL Server};'
					  	'Server=DESKTOP-LEGECK4;'
					  	'Database=Test;'
					  	'Trusted_Connection=yes;')
	mycursor = conn.cursor()
	# mycursor.execute("select * from users where bname=? and password=?",(userinput.get(),passinput.get()))
	# results = mycursor.fetchall()
	# if results:
	# 	#tk.messagebox.showinfo("","Login Success")
	# 	call(["python", "call files/new.py"])
	# 	return True
	# else:
	# 	#tk.messagebox.showinfo("","Login incorrect password")
	# 	Label(root, text="Please enter a correct username and password",font=("Goudy old style",15,"bold"),fg='red',bg='#95baa8').place(x=480, y=530)
	# 	return False
	

	mycursor = conn.cursor()
	mycursor.execute("select * from usernames where bname=? and password=?",(userinput.get(),passinput.get()))
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
# rot_i = Image.open("image/in1.png")
# rotunda = ImageTk.PhotoImage(rot_i)
# label = tk.Label(image=rotunda,bg='#3a3947')
# label.image = rotunda
# label.place(x=0, y=0)


root.geometry("{0}x{0}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(bg='#0B5A81')
color_me = Label(root, text='(217, 217, 217) #d9d9d9',font = ('Times', 20),relief = SOLID,padx=20, pady=20)
color_me = Label(root, text='(217, 217, 217) #d9d9d9',font = ('Times', 20),relief = SOLID,padx=20, pady=20)

# rot_i = Image.open("image/Sagacity.jpg")
# rotunda = ImageTk.PhotoImage(rot_i)
# label = tk.Label(image=rotunda)
# label.image = rotunda
# label.place(x=0, y=0)

root.attributes('-fullscreen',True)
frame_login=Frame(root, bg='#95baa8', highlightbackground="black", highlightthickness=5).place(height=320,width=530,x=430,y=255)
title=Label(frame_login ,text="login here",font=("Impact",35,"bold"),fg='#d77337',bg='#95baa8').place(x=600,y=260)

user_input=tk.StringVar()
pass_input=tk.StringVar()
userinput = Entry(root, textvariable=user_input,bg='light grey',font=15)
if userinput.get() == "":
	warn = "Contact can't be empty"


	
userinput.place(x=600, y=325,height=22,width=280)
passinput = Entry(root, textvariable=pass_input,bg='light grey',font=15)
passinput.place(x=600, y=350,height=22,width=280)
passinput.config(show="*")
Label(root, text="Username",font=("Goudy old style",15,"bold"),fg='black',bg='#95baa8').place(x=480, y=325)
Label(root, text="Password",font=("Goudy old style",15,"bold"),fg='black',bg='#95baa8').place(x=480, y=350)
#Label(root, text="Please enter a correct username and password",font=("Goudy old style",15,"bold"),fg='black',bg='#95baa8').place(x=480, y=530)



# def changeOnHover(Button, colorOnHover, colorOnLeave):
# 	Button("<Enter>", func=lambda e: Button.config(background=colorOnHover))
# 	Button("<Leave>", func=lambda e: Button.config(background=colorOnLeave))


photo = PhotoImage(file = r"image/Untitled (2).png")
Button(root,image = photo,command=lambda: root.quit(),bd=2,bg="grey",fg="red",highlightcolor="purple",activeforeground="green",activebackground="grey",  relief="groove",width = 9,height =1,font=("times new roman",12)).place(x=250, y=200)
exit_button = Button(root,text='Cancel',command=lambda: root.quit(),bd=2,bg="grey",fg="red",highlightcolor="purple",activeforeground="green",activebackground="grey",  relief="groove",width = 9,height =1,font=("times new roman",12)).place(x=750, y=400)
login_button = Button(root,  text="Login", command= lambda:[Ok()],bd=2,bg="grey",fg="red",  relief="ridge",width = 9,height =1,font=("times new roman",12,"bold")).place(x=600, y=400)
#-------------------Label Time----------------
def my_time():
    time_string = strftime('%H:%M:%S %p') # time format 
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds 
my_font=('times',14,'bold') # display size and style
l1=tk.Label(root,font=my_font,bg='#0B5A81')
l1.grid(row=1,column=1,padx=5,pady=25)
my_time()
#-------------------Label Time----------------

root.mainloop()




