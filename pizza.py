# Adding Radio Buttons for Pizza type
# Developer: Khom
# @ikhomkodes
# Date: Monday, 5 April 2021

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Coding with iKhom!')
# root.iconbitmap('/home/ikhom/PycharmProjects/tkinterGUI/DiUVXIFVQAE_ePs.jpg')

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()

# root.mainloop() # alternatively mainloop() only
mainloop()
