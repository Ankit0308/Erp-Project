from tkinter import *
from time import strftime
import tkinter as tk
root = Tk()
def my_time():
    time_string = strftime('%H:%M:%S %p') # time format 
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds 
my_font=('times',14,'bold') # display size and style
l1=tk.Label(root,font=my_font,bg='#95baa8')
l1.grid(row=0,column=1,padx=5,pady=5)
my_time()
root.mainloop()
