# importing nessessary modules in our program
from tkinter import *
import tkinter.messagebox as msg

# creating root as Tk class and updating default window size, maximum and minimum size with title of our GUI application
root = Tk()
root.geometry("655x333")
root.maxsize(655, 333)
root.minsize(655, 333)
root.title("ScrollBar using Tkinter")

# creating a Scrollbar and packing it with pack attribute
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# creating a Listbox and Filling some data within it
lbx = Listbox(root, yscrollcommand = scrollbar.set)
for i in range(344):
    lbx.insert(END, f"Item {i}")

# attaching our scrollbar with Listbox we created
lbx.pack(fill=Y)
scrollbar.config(command=lbx.yview)

# making our GUI program to run in a event loop
root.mainloop()
