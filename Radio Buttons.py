# importing nessessary modules in our program
from tkinter import *
import tkinter.messagebox as msg

# creating root as Tk class and updating default window size, maximum and minimum size with title of our GUI application
root = Tk()
root.geometry("655x333")
root.maxsize(655, 333)
root.minsize(655, 333)
root.title("Radio Buttons Using Tkinter In Python")

# creating a Label and Packing it with pack attribute
Label(root, text="What would you Like to have Sir!!", font="comicsansms 14 bold").pack()

# creating a Variable for storing a value
val = StringVar()

# setting its value with random word
val.set("sasti")

# creating a function which will perform its task when pressed
def order():
    msg.showinfo("Oder Sucessfull", f"You Have ordered {val.get()}. Thanks for Ordering")


# creating a RadioButton and packing it with pack attribute
var = Radiobutton(root, text="Dosa", variable = val, value="Dosa").pack(anchor="w")

# creating a RadioButton and packing it with pack attribute
var = Radiobutton(root, text="Paratha", variable = val, value="Paratha").pack(anchor="w")

# creating a RadioButton and packing it with pack attribute
var = Radiobutton(root, text="Chole Bhatoore", variable = val, value="Chole Bhatoore").pack(anchor="w")

# creating a RadioButton and packing it with pack attribute
var = Radiobutton(root, text="Samosa", variable = val, value="Samosa").pack(anchor="w")

# creating a Button and Packing it with Pack attribute
Button(root, text="Order Now", command=order).pack()

# creating a Button and Packing it with Pack attribute
Button(root, text="Quit", command=quit).pack(pady=30)

# making our GUI program to run in a event loop
root.mainloop()
