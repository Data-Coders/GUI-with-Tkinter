# importing nessesary modules in our program
from tkinter import *

# making root as a function in our program
root = Tk()

# setting the default height and width of our Application
root.geometry("655x333")

# updating the tittle of our Program
root.title("Buttons By Code With Harry")

# creating a frame and packing it
f1 = Frame(root, borderwidth=3)
f1.pack()

# creating a button on the frame we created and packing it with the help of frame we created
b1 = Button(f1, text="Print Now")
b1.pack(pady=142)

# making our app to go in a event loop
root.mainloop()