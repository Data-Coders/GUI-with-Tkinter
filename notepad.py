# importing nessesary modules in our GUI program
from tkinter import *
import tkinter.messagebox as msg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

# creating root as Tk class and updating default window size with title and icon of our GUI application
root = Tk()
root.geometry("655x333")
root.title("Notepad By Aman Ojha")
root.wm_iconbitmap("icon.ico")

# creating functions which will perform after they are pressed while they will be present under File heading of our GUI menu bar

# creating function which will create a new file when selected
def new():
    global file
    root.title("Untitled - By Aman Ojha")
    file = None
    text.delete(1.0, END)

# creating a function which will open a file when Selected 
def Open():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - By Aman Ojha")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()

# creating a function which will save the edited file when selected
def Save():
    global file
    if file == None:
        file = asksaveasfilename(initialfilename='Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents","*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + ' - By Aman Ojha')

# creating a function which will exit the GUI application when selected
def Exit():
    quit(0)

# creating a Menubar
menubar = Menu(root)

# adding a Option into our Menubar
file = Menu(menubar, tearoff=0)

# adding a feature into our menubar Option
file.add_command(label="New", command=new)

# adding a feature into our menubar Option
file.add_command(label="Open", command=Open)

# adding a feature into our menubar Option
file.add_command(label="Save", command=Save)

# adding seperator
file.add_separator()

# adding a feature into our menubar Option
file.add_command(label="Exit", command=Exit)

# cascading the feature under the main menu bar which we created
menubar.add_cascade(label='File', menu=file)

# creating functions which will perform when pressed while they will be present under Edit section in our GUI program

# creating function to cut the Selectedtext in the text area
def Cut():
    text.event_generate(("<<Cut>>"))

# creating a function which will copy the selected text from the text area
def Copy():
    text.event_generate(("<<Copy>>"))

# creating a function which will paste the copied text from the clipboard to the Text area
def Paste():
    text.event_generate(("<<Paste>>"))


# adding a Option into our Menubar
edit = Menu(menubar, tearoff=0)

# adding a feature into our menubar Option
edit.add_command(label="Cut", command=Cut)

# adding a feature into our menubar Option
edit.add_command(label="Copy", command=Copy)

# adding a feature into our menubar Option
edit.add_command(label="Paste", command=Paste)

# adding a seperator in our Dropdown menubar
edit.add_separator()

# adding a feature into our menubar Option
edit.add_command(label="Exit", command=Exit)

# cascaing our dropdown menu with the main menu 
menubar.add_cascade(label='Edit', menu=edit)


# creating functions which will perform when pressed while they will be present under Edit section in our GUI program
def Get_The_Help():
    msg.showinfo("Get the Help By Aman Ojha", "You can Directly mail Your Problem to kristarice81@gmail.com")

def about():
    msg.showinfo("Notepad By Aman Ojha", "This Notepad is Created by Aman Ojha A.K.A. Alex Mercer")

# adding a Option into our Menubar
helpp = Menu(menubar, tearoff=0)

# adding a feature into our menubar Option
helpp.add_command(label="Get The Help", command=Get_The_Help)

# adding a feature into our menubar Option
helpp.add_command(label="About", command=about)

# adding a seperator in our Dropdown menubar
helpp.add_separator()

# adding a feature into our menubar Option
helpp.add_command(label="Exit", command=Exit)

# cascaing our dropdown menu with the main menu 
menubar.add_cascade(label='Help', menu=helpp)

# configuring our root menubar
root.config(menu=menubar)

# creating a Text area which will be the main feature of our GUI program
text = Text(root)

# packing the textarea with pack attribute
text.pack(expand=True, fill=BOTH)

# creating a Scrollbar and attaching it with our Text area
scroll = Scrollbar(text)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

# creating a global file variable with None context
file = None

# making our GUI program to go in a Event Loop
root.mainloop()
