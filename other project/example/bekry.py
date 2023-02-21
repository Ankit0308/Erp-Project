from tkinter import * 
from tkinter import ttk

win = Tk() 

pw = PanedWindow(orient ='vertical') 
#creating Button widget 
top = ttk.Button(pw, text ="Just Click Me!!!\nI am a Button") 
top.pack(side=TOP) 

#Adding button widget to the panedwindow 
pw.add(top) 

#Creating Checkbutton Widget 
bot = Checkbutton(pw, text="I am Checkbutton Choose Me!") 
bot.pack(side=TOP) 
pw.add(bot) 

label = Label(pw, text="I am a Label") 
label.pack(side=TOP) 

pw.add(label) 

string = StringVar() 

entry = Entry(pw, textvariable=string, font=('arial', 15, 'bold')) 
entry.pack() 

# This is used to force focus on particular widget 
# that means widget is already selected for some operations 
entry.focus_force() 

pw.add(entry) 
pw.pack(fill = BOTH, expand = True) 

# To show sash 
pw.configure(sashrelief = RAISED) 

mainloop()