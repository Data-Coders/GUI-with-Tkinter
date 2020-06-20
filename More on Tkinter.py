# importing nessesary modules in our Program
from tkinter import *
import time

# creating root as Tk class and updating default window size, maximum and minimum size with title of our GUI application
root = Tk()
root.geometry("655x333")
root.maxsize(655, 333)
root.minsize(655, 333)
root.title("Status Bar using Tkinter")

# changing the icon of the GUI application
root.wm_iconbitmap("icon.ico")

# making our GUI application to run in a event loop
root.mainloop()