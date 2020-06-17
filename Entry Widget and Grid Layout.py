from tkinter import *

root = Tk()
root.geometry("655x333")
root.maxsize(655, 333)
root.minsize(655, 333)
root.title("Entry Widget and Grid Layout")

user = Label(text="UserName : ")
password = Label(text="Password : ")
user.grid()
password.grid(row=1)

# Variable classes in tkinter
# IntVar, BooleanVar, DoubleVar, StringVar

uservalue = StringVar()
userpass = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=userpass)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1, padx=180)

root.mainloop()
