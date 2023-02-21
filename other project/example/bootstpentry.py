import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox as m_box
import pyodbc

db = pyodbc.connect('Driver={SQL Server};'
					  'Server=DESKTOP-LEGECK4\ANKIT;'
					  'Database=test;'
					  'Trusted_Connection=yes;')
cursor = db.cursor()


class DataEntryForm(ttk.Frame):


    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.name = ttk.StringVar(value="")
        self.fullname = ttk.StringVar(value="")
        self.password = ttk.StringVar(value="")
        self.phone = ttk.StringVar(value="")

        # form header
        hdr_txt = "Please enter your contact information" 
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # form entries
        self.create_form_entry("Fullname", self.fullname)
        self.create_form_entry("Username", self.name)
        self.create_form_entry("Password", self.password)
        self.create_form_entry("Phone", self.phone)
        self.create_buttonbox()

    def create_form_entry(self, label, variable):
        """Create a single form entry"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_buttonbox(self):
        """Create the application buttonbox"""
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))
        
        sub_btn = ttk.Button(
            master=container,
            text="Submit",
            command=self.save,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Cancel",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)
    def save(self):
        fullname = self.fullname.get()
        name = self.name.get()
        password = self.password.get()
        phone = self.phone.get()
        if name == '' :
            m_box.showerror('Warning','Can not Blank Username')
        elif password == '':
            m_box.showinfo('Warning','Please Enter Password')
        else :
            try:
                name = str(name)
                cursor.execute("insert into sabusers (fullname, bname, password,phone,pid) values ('{}', '{}', '{}','{}',NEXT VALUE FOR SABUSERS_Sequence)".
                       format(fullname,name,password,phone ))
            except ValueError:
                m_box.showinfo('Error','Password Can not be strong')
        db.commit()


    def on_cancel(self):
        """Cancel and close the application."""
        self.quit()


if __name__ == "__main__":

    app = ttk.Window("User Master", "superhero", resizable=(False, False))
    DataEntryForm(app)
    app.mainloop()