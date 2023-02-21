
from http import server
from lib2to3.pgen2 import driver
import tkinter as tk
import ttkbootstrap as tttk
from ttkbootstrap.constants import *
from tkinter import messagebox as m_box
from tkinter.ttk import Style
from tkinter.ttk import *
from tkinter import ttk
from turtle import update
from typing_extensions import Self
import pyodbc
from random import randint

con1 = pyodbc.connect('Driver={SQL Server};'
    					  'Server=DESKTOP-LEGECK4\ANKIT;'
    					  'Database=test;'
    					  'Trusted_Connection=yes;')
cursor = con1.cursor()


class Example:
    cursor.execute("drop TABLE IF EXISTS EMPLOYEE")
# Create table as per requirement
    sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

    cursor.execute(sql)
#     Style.configure('TButton', font =
# 			('calibri', 20, 'bold'),
# 					borderwidth = '4')

# # Changes will be reflected
# # by the movement of mouse.
#     Style.map('TButton', foreground = [('active', '!disabled', 'green')],
# 					background = [('active', 'black')])

    

#---------------
    def __init__(self):
        window.title('Insert Data')
        window.geometry('500x400')
        window.wm_minsize(700, 400)

        self.Quitbtn = ttk.Button(window, text='Quit', command=self.close)
        self.Quitbtn.place(x=415, y=365
        )

        self.save_btn = ttk.Button(window, text='Save', command=self.save)
        self.save_btn.place(x=330, y=365)

        self.update_btn = ttk.Button(window, text='Update', command=self.update)
        self.update_btn.place(x=235, y=365)

# Bootstrap Labels ------------------------------------------
        tttk.Label()

# danger colored label style
        #tttk.Label(bootstyle="danger")
        tttk.Label(bootstyle="inverse")

# User Labels ------------------------------------------
        self.name_label = tttk.Label(window,bootstyle="inverse-danger", text='Username')
        self.name_label.place(x=20, y=50)
        
        
        self.family_label = ttk.Label(window, text='Password')
        self.family_label.place(x=20, y=100)

        self.phone_label = ttk.Label(window, text='Sabid')
        self.phone_label.place(x=20, y=150)
# Update Labels ------------------------------------------
        self.name_label = ttk.Label(window, text='Sabid')
        self.name_label.place(x=240, y=50)
    
    
        def validate_number(x) -> bool:
            """Validates that the input is a number"""
            if x.isdigit():
                return True
            elif x == "":
                return True
            else:
                return False
    
        def validate_alpha(x) -> bool:
            """Validates that the input is alpha"""
            if x.isdigit():
                return False
            elif x == "":
                return True
            else:
                return True      
            # register the validation callback
        digit_func = tttk.register(validate_number)
        #alpha_func = tttk.register(validate_alpha)  

# Entry -------------------------------------------
        tleft2 = tk.IntVar()
        global tleft2_entry
        tleft2_entry = tk.Entry(window, validate="focus", validatecommand=(digit_func, '%P'), textvariable=tleft2, width=20)
        tleft2_entry.place(x=100, y=150)
        
        name = tk.StringVar()
        global name_entry
        tleft1=tleft2.get()
        name_entry = tk.Entry(window, validate="focus", validatecommand=(digit_func, '%P'), textvariable=name, width=20)
        name_entry.place(x=100, y=50)
        
        family = tk.StringVar()
        global family_entry
        family_entry = tk.Entry(window, validate="focus", validatecommand=(digit_func, '%P'),textvariable=family, width=20)
        family_entry.place(x=100, y=100)
        
        phone = tk.IntVar()
        global phone_entry
        #phone_entry = tk.Entry(window, textvariable=phone, width=20)
        phone_entry = ttk.Entry(window, validate="focus",textvariable=phone, width=20, validatecommand=(digit_func, '%P'))
        phone_entry.place(x=100, y=150)
#update Entry -------------------------------------------
        bcode = tk.StringVar()
        global bcode_entry
        bcode_entry = tk.Entry(window, validate="focus", validatecommand=(digit_func, '%P'), textvariable=bcode, width=20)
        bcode_entry.place(x=350, y=50)

        ttop = tk.StringVar()
        global ttop_entry
        ttop_entry = tk.Entry(window,  validate="focus", validatecommand=(digit_func, '%P'),textvariable=ttop, width=20)
        ttop_entry.place(x=350, y=100)
        

        tleft = tk.IntVar()
        global tleft_entry
        tleft_entry = tk.Entry(window, validate="focus", validatecommand=(digit_func, '%P'), textvariable=tleft, width=20)
        tleft_entry.place(x=350, y=150)
    @staticmethod
    # def X():
    #     ttop1 = ttop_entry.get()   
    #     cursor.execute("insert into sabtopleft (ttop) values ('{}')".
    #                    format(ttop1))
    #     db.commit()
    #     tk.Label(window, text='Ttop Successfully!', fg='red', font=20).place(x=75, y=350)

    
     


    @staticmethod
    def update():
        bcode = bcode_entry.get()
        ttop = ttop_entry.get()
        tleft = tleft_entry.get()
        if bcode == '' :
            m_box.showerror('Warning','Can Not be Blank Bcode')
        elif ttop == '' or ttop == 0:
            m_box.showwarning('Warning','Can Not be Blank Ttop')
        elif tleft == '' or tleft == 0:
            m_box.showinfo('Warning','Can Not be Blank tleft')

        else :
            try:
                ttop = int(ttop)
                cursor.execute("insert into sabtopleft (bcode, ttop, tleft,rowid,pid) values ('{}', '{}', '{}',NEXT VALUE FOR SabTopLeft_Sequence,NEXT VALUE FOR SabTopLeft_Sequence)".
                       format(bcode, ttop, tleft))
            except ValueError:
                m_box.showinfo('Error','only integer value type')

            

        
        db.commit()
        #tk.Label(window, text='Insert Successfully Data!', fg='red', font=20).place(x=75, y=350)
#number = int(input("Enter a number: "))
    @staticmethod
    def close():
        db.close()
        window.quit()

    @staticmethod
    def save():
        name = name_entry.get()
        family = family_entry.get()
        phone = phone_entry.get()
        if name == '' :
            m_box.showerror('Warning','Can not Blank Username')
        
        elif family == '':
            m_box.showinfo('Warning','Please Enter Password')

        else :
            try:
                name = str(name)
            except ValueError:
                m_box.showinfo('Error','only character value type')
       
        cursor.execute("insert into usernames (bname, password, sabid) values ('{}', '{}', NEXT VALUE FOR username_Sequence)".
                       format(name, family, phone))
        db.commit()

        

        

        tk.Label(window, text='Saved Successfully!', fg='green', font=20).place(x=100, y=350)

window = tk.Tk()

lab = Label(window)
lab.pack()
def update():
   lab['text'] = randint(0,1000)
   window.after(1000, update) # run itself again after 1000 ms


obj = Example()  # object instantiated
window.mainloop()

