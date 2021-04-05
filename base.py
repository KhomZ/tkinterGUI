# Create new Windows
# Developer: Khom
# @ikhomkodes
# Date: Monday, 5 April 2021

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Coding with iKhom!')
# root.iconbitmap('/home/ikhom/PycharmProjects/tkinterGUI/DiUVXIFVQAE_ePs.jpg')


def open():
    global my_img
    top = Toplevel()
    top.title("My Second Window")
    # top.iconbitmap('/home/ikhom/PycharmProjects/tkinterGUI/DiUVXIFVQAE_ePs.jpg')
    my_img = ImageTk.PhotoImage(Image.open("images/ikhomkodes.png"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="Close window", command=top.destroy).pack()


btn = Button(root, text="Open Second Window", command=open).pack()

# root.mainloop() # alternatively mainloop() only
mainloop()
