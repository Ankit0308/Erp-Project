from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import tkinter as tk
from tkinter import END
def show_data():
    #create the mysql connection string by using entry box inputs 
    str1="mysql+mssqldb://"+userid.get()+":" \
        +pw.get()+"@"+host.get()+"/"+db.get()
    #print(str1) # check the string 
    t1.delete('1.0',END)# Remove the previous data 
    t1.update()    
    my_output='' # set a blank string 
    try:
        my_conn=create_engine(str1) # try to connect
        r_set=my_conn.execute("SHOW TABLES") #query to run

        for i in r_set:
            my_output= my_output + str(i[0]) + '\n'
        t1.config(bg='black') # update background colour 
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        my_output=error
        t1.config(bg='yellow',font=('Times',16,'normal'))#error format
        #print(error)    
    t1.insert(tk.END, my_output) # add the output to Entry widget

### layout design of the widgets in window ##
my_w = tk.Tk()
my_w.geometry("600x420") # width & hieght of window
l1=tk.Label(my_w,text='Host')
l1.grid(row=1,column=1,padx=5)
host=tk.StringVar()
host.set('localhost') # default value, change if required
e1=tk.Entry(my_w,textvariable=host,width=10)
e1.grid(row=1,column=2)

l2=tk.Label(my_w,text='Database')
l2.grid(row=1,column=3,padx=5)
db=tk.StringVar()
db.set('')
e2=tk.Entry(my_w,textvariable=db,width=10)
e2.grid(row=1,column=4)

l3=tk.Label(my_w,text='userid')
l3.grid(row=1,column=5,padx=5)
userid=tk.StringVar()
userid.set('')
e3=tk.Entry(my_w,textvariable=userid,width=10)
e3.grid(row=1,column=6)

l4=tk.Label(my_w,text='Password')
l4.grid(row=1,column=7,padx=5)
pw=tk.StringVar()
pw.set('')
e4=tk.Entry(my_w,textvariable=pw,show='*',width=10)
e4.grid(row=1,column=8)

b1=tk.Button(my_w,text='Connect',width=10,command=lambda:show_data())
b1.grid(row=1,column=9)
t1=tk.Text(my_w,height=20,width=40)
t1.grid(row=2,column=1,columnspan=8)
my_w.mainloop()