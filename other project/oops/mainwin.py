from operator import truediv
import tkinter as tk
from tkinter import ttk

class mainwindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.username = 'coolusername'
        frame_main = ttk.Frame(self)
        frame_main.pack(fill='both',expand=True)
        btn_show_username = ttk.Button(frame_main,text='show data',command=self.show_username)
        btn_show_username.pack(padx=10,pady=10)
    
    def show_username(self):
        username_window=usernamewindow(self,username=self.username)

class usernamewindow(tk.Toplevel):
    def __init__(self, master,username):
        super().__init__()
        self.username = username
        self.frame_main = ttk.Frame(self)
        self.frame_main.pack(fill=tk.BOTH,expand=True)

        lbl_username = tk.Label(self.frame_main,text=f"my user:{self.username}")
        lbl_username.pack(padx=50,pady=50)
if __name__=="__main__":
    main_windodw = mainwindow()
    main_windodw.mainloop()

