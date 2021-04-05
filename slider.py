# Creating Sliders
# Developer: Khom
# @ikhomkodes
# Date: Monday, 5 April 2021

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code with ikhomkodes')
# root.iconbitmap('/home/ikhom/PycharmProjects/tkinterGUI/DiUVXIFVQAE_ePs.jpg')
root.geometry("400x400")


vertical = Scale(root, from_=0, to=200, orient=VERTICAL)
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()


def vert_slide():
    my_label = Label(root, text=vertical.get()).pack()
    root.geometry(str(vertical.get()) + "x400")


def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x400")


my_btn1 = Button(root, text="Click Me for change in height!", command=vert_slide).pack()
my_btn2 = Button(root, text="Click Me for change in width!", command=slide).pack()

mainloop()
