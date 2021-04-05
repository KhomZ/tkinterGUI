# Adding Radio Buttons
# Developer: Khom
# @ikhomkodes
# Date: Monday, 5 April 2021

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Coding with iKhom!')
# root.iconbitmap('/home/ikhom/PycharmProjects/tkinterGUI/DiUVXIFVQAE_ePs.jpg')

r = IntVar()
# r.set("2")


# defining clicked function
def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get(1))).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get(1))).pack()


myLabel = Label(root, text=r.get())
myLabel.pack()

myButton = Button(root, text="Click Me!", command=lambda: clicked(r.get()))
myButton.pack()

# root.mainloop() # alternatively mainloop() only
mainloop()
