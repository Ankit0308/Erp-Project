import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Position text in frame
Label(root, text = 'Position image on button', font =('<font_name>', 13)).pack(side = TOP, padx = 0.5, pady = 0.5)

# Create a photoimage object of the image in the path
photo = PhotoImage(file = "E:/image.png")

# Resize image to fit on button
photoimage = photo.subsample(1, 1)

# Position image on button
Button(root, image = photoimage,).pack(side = BOTTOM, pady = 10)
mainloop()