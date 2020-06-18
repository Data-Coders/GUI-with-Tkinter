from tkinter import *

root = Tk()
root.geometry("655x333")
root.minsize(655, 333)
root.maxsize(655, 333)
root.title("Menu and Sub Menus in Tkinter")


# non dropdown menu
# def file():
#     print('It works')
# mymenu = Menu(root)
# mymenu.add_command(label='File', command=file)
# mymenu.add_command(label='Exit', command=quit)
# root.config(menu=mymenu)

# Dropdown Menubar
def hello():
    print('It works')


mymenu = Menu(root)
file = Menu(mymenu, tearoff=0)
file.add_command(label='New Project', command=hello)
file.add_separator()
file.add_command(label='New', command=hello)
file.add_command(label='New Scratch File', command=hello)
file.add_separator()
file.add_command(labe='Open', command=hello)
mymenu.add_cascade(label="File", menu=file)
root.config(menu=mymenu)

root.mainloop()
