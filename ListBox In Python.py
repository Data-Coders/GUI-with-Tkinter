# importing nessesary modules in our Program
from tkinter import *
import tkinter.messagebox as msg

# making root variable as Tk class and Updating Title, minimum and maximum size and Title of our GUI application
root = Tk()
root.geometry("655x333")
root.maxsize(655, 333)
root.minsize(655, 333)
root.title("ListBox using Tkinter")

# creating a function which will be called when the Button is Pressed
def ad():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i = i+1

# creating a global variable i 
i = 0

# creating a Listbox and packing It
lbx = Listbox(root)
lbx.pack(ipadx=20)

# inserting a default item in the ListBox
lbx.insert(END, "First Item of this List Box")

# creating a Button and packing it
Button(root, text="Add Item", command=ad).pack()

making our GUI program to run into a Event Loop
root.mainloop()
