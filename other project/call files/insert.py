import tkinter as tk
from tkinter import messagebox
import pyodbc  

class insertdata:
    def Ok():
        conn = pyodbc.connect('Driver={SQL Server};'
					  'Server=DESKTOP-LEGECK4;'
					  'Database=test;'
					  'Trusted_Connection=yes;')