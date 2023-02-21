import tkinter.ttk as ttk
import tkinter as tk
import pyodbc




    
def connect():
    con1 = pyodbc.connect('Driver={SQL Server};'
					  'Server=DESKTOP-LEGECK4\ANKIT;'
					  'Database=test;'
					  'Trusted_Connection=yes;')
    cursor = con1.cursor()

    cur1 = con1.cursor()
    
def View():  
    con1 = pyodbc.connect('Driver={SQL Server};'
    					  'Server=DESKTOP-LEGECK4\ANKIT;'
    					  'Database=test;'
    					  'Trusted_Connection=yes;')
    cursor = con1.cursor()
    
    cur1 = con1.cursor()
       
    f = open("sdl\sqlquery.sdl","r")
    f1=f.read()


    cur1.execute(f1)
    
    rows = cur1.fetchall()    
    
    for row in rows:
        tree.insert("", tk.END, values=row)
    


    con1.close()
    
    
    # connect to the database
    
connect() 
    
root = tk.Tk()
    
tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4", "c5", "c6","c7", "c8", "c9","c10", "c11", "c12"))

tree.pack(padx=20,pady=10)

   

tree.column("#1", anchor=tk.CENTER)
    
tree.heading("#1", text="bname")
    
tree.column("#2", anchor=tk.CENTER)
    
tree.heading("#2", text="fullname")
    
tree.column("#3", anchor=tk.CENTER)
    
tree.heading("#3", text="pid")
    
#tree.pack(padx=10,pady=5)

    
button1 = tk.Button(text="Display data", command=View)
    
button1.pack(pady=10)

root.mainloop()
