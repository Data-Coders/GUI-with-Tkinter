# importing nessessary modules in our program
from tkinter import *
import time

# creating root as Tk class and updating default window size, maximum and minimum size with title of our GUI application
root = Tk()
root.geometry("655x333")
root.maxsize(655, 333)
root.minsize(655, 333)
root.title("Status Bar using Tkinter")

# creating functions which is going to perform when the respective Buttons are pressed
def upload():
    stx.set("Busy...")
    stb.update()
    time.sleep(2)
    stx.set("Ready")

# creating a Variable which will store some string in it
stx = StringVar()

# giving value to our variable
stx.set("Ready")

# creating a button and packing it
Button(root, text="Upload", command=upload).pack()

# creating a label
stb = Label(root, textvariable=stx, relief=SUNKEN, anchor="w")

# packing the label
stb.pack(side=BOTTOM, fill=X)

# making our program to run in a eventloop
root.mainloop()
