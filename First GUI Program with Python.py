# Importing the Tkinter Framework
from tkinter import *

# making the root variable as Tk Class
root = Tk()

# Logic for GUI goes down here

# creating a Label Variable and giving some text into it
label = Label(text='Hii This is the First GUI program In Python and a Start of 100 Days of Python')

# Packing the Label Variable to get the Variable on to the root Variable
label.pack()

# Packing the GUI interface with a 500 x 500 size
root.geometry("733x434")

#Minimum size for the GUI interface
root.minsize(733, 434)

# Max size for the GUI interface
root.maxsize(733, 434)

# Logic Ends Here

# Making our GUI program to run in a Countless number of Event
root.mainloop()