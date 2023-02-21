from tkinter import *
import pyodbc

#Create application and size
root = Tk()
root.title('Application')
root.geometry("400x400")

# Connect to SQL Server database
conn = pyodbc.connect('Driver={SQL Server};'
					  'Server=DESKTOP-LEGECK4;'
					  'Database=test;'
					  'Trusted_Connection=yes;')
#Create cursor
cursor = conn.cursor()
cursor.execute('SELECT * FROM ASAB9')

#Create submit function for database
def submit():
# Connect to SQL Server database
	conn = pyodbc.connect('Driver={SQL Server};'
					  'Server=DESKTOP-LEGECK4;'
					  'Database=test;'
					  'Trusted_Connection=yes;')
# Create cursor
	cursor = conn.cursor()
# Insert into table
	cursor.execute("INSERT INTO ASAB9 VALUES (:EquipmentName, :HostName, :ValidationName)",
               {
                   'EquipmentName': EquipmentName.get(),
                   'HostName': HostName.get(),
                   'ValidationName': ValidationName.get()
               })
# Commit changes
	conn.commit()

# Close connection
	conn.close()

# Clear the text boxes
	EquipmentName.delete(0, END)
	HostName.delete(0, END)
	ValidationName.delete(0, END)

# Create query function
def query():
# Connect to SQl Server DB
	conn = pyodbc.connect('Driver={SQL Server};'
					  'Server=DESKTOP-LEGECK4;'
					  'Database=test;'
					  'Trusted_Connection=yes;')

# Create cursor
	cursor = conn.cursor()
# Query the database
	cursor.execute("SELECT * FROM ASAB9")
	records = cursor.fetchall()
#print(records)

#Loop through results
	print_records = ''
	for record in records:
		print_records += str(record[0]) + " " +str(record[2]) + " " "\n"

	query_label = Label(root, text=print_records)
	query_label.grid(row=3, column=0, columnspan=2)

# Commit changes
	conn.commit()

# Close connection
	conn.close()

# Create text boxes
EquipmentName = Entry(root, width=30)
EquipmentName.grid(row=0, column=1, padx=20)

HostName = Entry(root, width=30)
HostName.grid(row=1, column=1)

ValidationName = Entry(root, width=30)
ValidationName.grid(row=2, column=1)

# Create labels for text boxes
EquipmentName_label = Label(root, text="Equipment Name")
EquipmentName_label.grid(row=0, column=0)

HostName_label = Label(root, text="Host Name")
HostName_label.grid(row=1, column=0)

ValidationName_label = Label(root, text="Validation Name")
ValidationName_label.grid(row=2, column=0)

# Create submit button to add entries
submit_btn = Button(root, text="Add record", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

# Create a query button
query_btn = Button(root, text="Show Records", command=query) 
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()