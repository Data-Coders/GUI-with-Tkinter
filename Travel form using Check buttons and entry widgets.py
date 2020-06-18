# importing nessesary modules
from tkinter import *

# setting the root variable and updating its basic context
root = Tk()
root.geometry("655x333")
root.minsize(655, 333)
root.maxsize(655, 333)
root.title("Travel form using Entry Widget and Check Buttons")

# Printing the Header of the Contact Form
Label(root, text="Welcome to Alex Travels", font="comicsansms 13 bold", pady=15).grid(row=0, column=4)

# creating labels for diffrent entry
name = Label(root, text="Name")
phone = Label(root, text="Phone Number : ")
gender = Label(root, text="Gender : ")
emergency = Label(root, text="Emergency Contact Number :")
paymentmode = Label(root, text="Payment Mode : ")

# Packing it onto the root variable with grid
name.grid(row=1, column=3)
phone.grid(row=2, column=3)
gender.grid(row=3, column=3)
emergency.grid(row=4, column=3)
paymentmode.grid(row=5, column=3)

# creating variables to store the Entered Value
nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
emergencyValue = StringVar()
paymentmodeValue = StringVar()
foodserviceVal = IntVar()

# Making a Entry widget for entering the  data Variable
nameEntry = Entry(root, textvariable=nameValue)
phoneEntry = Entry(root, textvariable=phoneValue)
genderEntry = Entry(root, textvariable=genderValue)
emergencyEntry = Entry(root, textvariable=emergencyValue)
paymentmodeEntry = Entry(root, textvariable=paymentmodeValue)

# Packing it with the help of grid
nameEntry.grid(row=1, column=4)
phoneEntry.grid(row=2, column=4)
genderEntry.grid(row=3, column=4)
emergencyEntry.grid(row=4, column=4)
paymentmodeEntry.grid(row=5, column=4)

# Creating a Checkbox and Packing it with grid
foodservice = Checkbutton(root, text="Want to Prebook the Meal now??", variable=foodserviceVal)
foodservice.grid(row=6, column=4)


# creating a function which will do command as directed by the Submit Button
def works():
    print("It works")
    with open("records.txt", "a") as f:
        f.write(f"{(nameValue.get(), phoneValue.get(), genderValue.get(), emergencyValue.get(), paymentmodeValue.get(), foodserviceVal.get(),)}\n")
        print(f"{(nameValue.get(), phoneValue.get(), genderValue.get(), emergencyValue.get(), paymentmodeValue.get(), foodserviceVal.get(),)}")


# Creating a Button and packing it with grid
Button(root, text="Submit to Alex Travels", command=works).grid(row=7, column=4)

# making our root variable to enter in a event-loop
root.mainloop()
