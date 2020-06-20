# importing nessessary modules in our program
from tkinter import *
import tkinter.messagebox as msg

# creating root as Tk class and updating default window size, maximum and minimum size with title of our GUI application
root = Tk()
root.geometry("655x333")
root.maxsize(655, 333)
root.minsize(655, 333)
root.title("Sliders using Tkinter")

# crreating a Frame and packing it with the pack attribute
file = Frame(root)
file.pack(pady=20)

# creating a Label and packing it in a single line with pack attribute
Label(file, text="How much Amount you Want to Be Credited in Your Bank Account??").pack()

# creating a slider
slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, width=10, length=300, tickinter=10)

# setting its default value
slider.set(50)

# packing it with packi atribute
slider.pack()

# creating functions which is going to perform when the respective Buttons are pressed
def msgg(num):
    print(num)
    msg.showinfo("info", f"Your Entered Bank Account Number is : {num}")
    if num == 56:
        msg.showinfo("Amount Credited", f"We have Successfully Credited {slider.get()} Rupees in your Respective Account")

    else:
        pass

# creating functions which is going to perform when the respective Buttons are pressed
def msggg():
    msgg(56)

# creating functions which is going to perform when the respective Buttons are pressed
def getamount():
    var = Tk()
    label = Label(var, text = "Enter Your Bank Account Number : ")
    label.pack()
    varr = StringVar()
    en = Entry(var, textvariable=varr)
    en.pack()
    print("Working")
    msgg(varr.get())
    Button(var, text="Submit", command=msggg).pack()
    var.mainloop()


# creating a Frame and packing it
edit = Frame(root)
edit.pack(pady = 20)

# creating a Button and packing it
Button(edit, text="Get Ammount", command=getamount).pack()

# making our program run in a event loop
root.mainloop()
