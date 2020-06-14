# Importing the Tkinter FrameWork
from tkinter import *

# Importing The Classes from Pillow Framework
from PIL import ImageTk, Image

# making root as Tk function
root = Tk()

# making a Image viewer GUI application on Default Size
# root.geometry('1920x1080')

# making Image Viewer Default Size as width as 900 and Height as 500
root.geometry('900x500')

# making Image Viewer Minimum Size as width as 900 and Height as 500
root.minsize(900, 500)

# making Image Viewer Maximum Size as width as 900 and Height as 500
root.maxsize(900, 500)

# opening Image file in and storing the image state in Image Variable
image = Image.open('665093.jpg')

# Saving The Image State in photo Variable with the help of PhotoImage Function
photo = ImageTk.PhotoImage(image)

# making Our Image as a Label
label = Label(image=photo)

# Packing the Label onto the Root Variable
label.pack()

# Making our GUI Application run continously
root.mainloop()