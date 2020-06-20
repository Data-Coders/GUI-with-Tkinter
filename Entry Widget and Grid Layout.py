# importing nesessary modules in our program
from tkinter import *

# making root as a function as Tk is
root = Tk()

# updating title, maximum, minimum, and default window size of our application
root.geometry("655x333")
root.maxsize(655, 333)
root.minsize(655, 333)
root.title("Entry Widget and Grid Layout")

# creating Labels and packing it with the help of grid
user = Label(text="UserName : ")
password = Label(text="Password : ")
user.grid()
password.grid(row=1)

# Variable classes in tkinter
# IntVar, BooleanVar, DoubleVar, StringVar

# creating two variable to store the data entered through GUI program
uservalue = StringVar()
userpass = StringVar()

# creating two Entry where the user will enter its data
userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=userpass)

# packing the entry with the help of grid
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1, padx=180)

# making our Application to go in a Event Loop
root.mainloop()
