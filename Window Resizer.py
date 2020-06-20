# importing nessessary modules in our program
from tkinter import *
import tkinter.messagebox as msg

# creating root as Tk class and updating default window size, maximum and minimum size with title of our GUI application
root = Tk()
root.geometry("360x168")
root.minsize(360, 168)
root.title("Window Resizer")

# creating a Label and apcking it with help of Grid
Label(root, text="Welcome to Window Resizer", font="comicsansms 19 bold").grid()

# creating functions which is going to perform when the respective Buttons are pressed
def resize():
    root.geometry(f"{hei.get()}x{wid.get()}")

# creating a variable which will store the value when enterd
hei = IntVar()
wid = IntVar()

# creating a Entry where the data will be entered
he = Entry(root, textvariable = hei)
wi = Entry(root, textvariable = wid)

# packing the entry with the help of grid
he.grid(pady=10)
wi.grid(pady=10)

# craeting a Button and and packing it with the help of grid
Button(root, text = "Resize", command = resize).grid(pady=10)

# making our program to run in a Event Loop
root.mainloop()
