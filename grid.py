# Positioning with Tkinter's Grid System
# @author: ikhomkodes

from tkinter import *

root = Tk()

newLabel1 = Label(root,text="Hello ikhomkodes!!!")
newLabel2 = Label(root,text="My name is Khom Raj Thapa Magar")

newLabel1.grid(row=0, column=0)
newLabel2.grid(row=1, column=1)


root.mainloop()

# Python is an object-oriented programming language
# Everything is a two-step process
# -->> create things
# -->> put the things on the screen
