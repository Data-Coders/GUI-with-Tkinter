# Importing necesary modules to our Program
from tkinter import *
import time

# making root as tk function
root = Tk()

# updating geometry of our window
root.geometry("655x333")

# setting max and min size of our window
root.minsize(655, 333)
root.maxsize(655, 333)

# updating the title of our window
root.title("Question 2 by Code with Harry")

# Question starts from here

# label of our question
question = Label(text="Question is :-")

# packing it on to the root window
question.pack(side=LEFT, anchor="ne", pady=20)

# Question label created
main_question = Label(
    text="Create For button in GUI using Python Tkinter and give each button a command to print something")

# packing it onto the root variable
main_question.pack(side=TOP, pady=35)

# Question ends Here

# Solution starts here

# funtion1 or command1
def first():
    print("This is the first one")

# function2 or command2
def second():
    print("This is the second one")

# function3 or command3
def third():
    print("This is the third one")

# function4 or command4
def fourth():
    print("This is the fourth one")

a = True

# funtion5 or command5
# testing some automation here
def fifth():
    while(a == True):
        first()
        time.sleep(1)
        second()
        time.sleep(1)
        third()
        time.sleep(1)
        fourth()
        time.sleep(1)

# created some buttons and gave them their respective commands
b1 = Button(text="First", command=first)
b2 = Button(text="Second", command=second)
b3 = Button(text="Third", command=third)
b4 = Button(text="Fourth", command=fourth)
b5 = Button(text="Fifth", command=fifth)
b6 = Button(text="Quit", command=exit)

# packed all the buttons onto the root variable of our window
b1.pack(side=LEFT, padx=3)
b2.pack(side=TOP)
b3.pack(side=RIGHT)
b6.pack(side=TOP, pady=25)
b4.pack(side=BOTTOM)
b5.pack(pady=10)

# made the root variable to enter into the eventloop
root.mainloop()