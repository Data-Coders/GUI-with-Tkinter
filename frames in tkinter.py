# importing tkinter module
from tkinter import *

# making root variable as Tk function
root = Tk()

# updating geometry of root variable
root.geometry("655x333")

# setting minsize of our window
root.minsize(655, 333)

# updating the title of our window
root.title("Frames in Tkinter by Code with Harry")

# creating new frame on the root variable
f1 = Frame(root, bg="grey", borderwidth=3)

# packing the frame on the root variable
f1.pack(side=LEFT, fill=Y)

# creating new frame on the root variable
f2 = Frame(root, bg="grey", borderwidth=3)

# packing the frame on the root variable
f2.pack(side=TOP, fill=X)

# creating new frame on the root variable
f3 = Frame(root, bg="grey", borderwidth=3)

# packing the frame on the root variable
f3.pack(side=LEFT, fill=X)

# creating new label
labeof1 = Label(f1, text="This is Side bar")

# packing it with the help of frame 1 which is already on the root variable
labeof1.pack(pady=142)

# creating new frame
labelof2 = Label(f2, text="Welcome to Sublime Text 4")

# packing it with the help of frame 2 which is already on the root variable
labelof2.pack()

# creating new label
labelof3 = Label(f3, text="This is the main Content")

# packing it with the help of frame 3 which is already on the root variable
labelof3.pack()

# making our root variable to go in eventloop
root.mainloop()