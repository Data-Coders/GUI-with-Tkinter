# importing nessessary modules in our program
from tkinter import *
import tkinter.messagebox as msg

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

# cascaing our dropdown menu with the main menu 
mymenu.add_cascade(label="File", menu=file)

# configuring our menubar with main menu
root.config(menu=mymenu)

# creating functions which is going to perform when the respective Buttons are pressed
def cut():
    print("Edit")

def copy():
    print("Edit")

def paste():
    print("Edit")

def select():
    print("Edit")


# adding a Option into our Menubar
edit = Menu(mymenu, tearoff=0)

# adding a feature into our menubar Option
edit.add_command(label="Cut", command=cut)

# adding a feature into our menubar Option
edit.add_command(label="Copy", command=copy)

# adding a feature into our menubar Option
edit.add_command(label="Paste", command=paste)

# adding seperator
edit.add_separator()

# adding a feature into our menubar Option
edit.add_command(label="Select", command=select)

# cascaing our dropdown menu with the main menu 
mymenu.add_cascade(label="Edit", menu=edit)

# configuring the main menubar 
root.config(menu=mymenu)


# creating a function that will perform after the respective button is pressed
def helpp():

	# printing a dummy text while debugging
    print("Help")

    # getting the response from the user
    n = msg.askyesno("Want some help??", "Tell me where you got stuck. Alex will get back to you soon..")
    
    # checking the response got from the user
    if n == False:

    	# acting upon the reponse got from the user
        msg.askyesno("Tell me What do you want!!", "Tell me what you want")


# adding a Option into our Menubar
help = Menu(mymenu, tearoff=0)

# adding a feature into our menubar Option
help.add_command(label="Help", command=helpp)

# adding a feature into our menubar Option
mymenu.add_cascade(label="Help", menu=help)

# configuring the main menu of our Program
root.config(menu=mymenu)

# making our program to run in a event loop
root.mainloop()
