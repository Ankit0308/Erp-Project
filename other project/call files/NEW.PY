from cProfile import label
from logging import root
from tkinter import *
import tkinter as tk
import datetime as dt
from time import strftime

root = Tk()
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label='Exit',
    command=root.destroy
)



root.title("Login")
root.geometry("{0}x{0}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(bg='#0B5A81')

#date = dt.datetime.now()
# Create Label to display the Date
#label = Label(root, text=f"{date:%A, %B %d, %Y}", font="Calibri, 20").place(x=480, y=705)

#label.pack(pady=1)
# create a menubar



def openNewWindow():
	newWindow = tk.Toplevel(root)
	newWindow.title("New Window")
	newWindow.geometry("1199x600+100+50")

	label(newWindow,
		text ="This is a new window").pack()		
	button=button(newWindow, text="Close", command=newWindow.destroy)
	button.pack()
exit_button = Button(root,text='Cancel',command=lambda: root.quit(),bd=2,bg="grey",fg="red",highlightcolor="purple",activeforeground="green",activebackground="grey",  relief="groove",width = 9,height =1,font=("times new roman",12)).place(x=750, y=400)
#root.attributes('-fullscreen',True)

def my_time():
    time_string = strftime('%H:%M:%S %p') # time format 
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds 
	
my_font=('times',14,'bold') # display size and style
l1=tk.Label(root,font=my_font,bg='#0B5A81')
l1.grid(row=1,column=1,padx=5,pady=25)
my_time()

root.mainloop()

