import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="superhero")
# default date entry
ttk.DateEntry()
# success colored date entry
bb1=ttk.DateEntry(bootstyle="readonly")
bb1.pack(side=LEFT, padx=10, pady=10)
b1 = ttk.Button(root, text="Submit", bootstyle="secondary")
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Submit", bootstyle="info-outline")
b2.pack(side=LEFT, padx=5, pady=10)

root.mainloop()