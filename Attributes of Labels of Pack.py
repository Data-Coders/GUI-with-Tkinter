# importing tkinter module
from tkinter import *

# making root as tk function
root = Tk()

# updating the geometry of our root function
root.geometry("444x223")

# updating title of our window application
root.title("My GUI with Harry")

# this is also the way of passing the font to the label
# font=("comicsansms", 9)

# Giving the attributes to label
labelof = Label(text="Alex Mercer and this is his learning tutorial of GUI programming with Tkinter in Python. Be sure to check everything in this series one by one.", bg="red", fg="white", font="comicsansms 9",borderwidth=3,relief=RIDGE)

# pack attributes
# anchor = northwest(nw)
# side = top, bottom, right, left
# fill
# padx
# pady






# packing the labelof variable on to the root window
labelof.pack(side=BOTTOM, fill=X)

# making the root window to run on a continueous loop
root.mainloop()