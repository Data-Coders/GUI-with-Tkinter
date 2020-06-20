# importing nessesary modules in our program
from tkinter import *

# creating root as Tk class and updating default window size, maximum and minimum size with title of our GUI application
root = Tk()
root.geometry("655x333")
root.minsize(655, 333)
root.maxsize(655, 333)
root.title("Menu and Sub Menus in Tkinter")

# non dropdown menu
# def file():
#     print('It works')
# mymenu = Menu(root)
# mymenu.add_command(label='File', command=file)
# mymenu.add_command(label='Exit', command=quit)
# root.config(menu=mymenu)

# Dropdown Menubar
def hello():
    print('It works')

# creating a Menubar
mymenu = Menu(root)

# adding a Option into our Menubar
file = Menu(mymenu, tearoff=0)

# adding a feature into our menubar Option
file.add_command(label='New Project', command=hello)

# adding a seperator in our dropdown menubar
file.add_separator()

# adding a feature into our menubar Option
file.add_command(label='New', command=hello)

# adding a feature into our menubar Option
file.add_command(label='New Scratch File', command=hello)

# adding a seperator in our Dropdown menubar
file.add_separator()

# adding a feature into our menubar Option
file.add_command(labe='Open', command=hello)

# adding a feature into our menubar Option
mymenu.add_cascade(label="File", menu=file)

# configuring our menubar with main menu
root.config(menu=mymenu)

# making our Program to run in a EventLoop
root.mainloop()