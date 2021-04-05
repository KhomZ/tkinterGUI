# Open Files Dialog Box
# Developer: Khom
# @ikhomkodes
# Date: Monday, 5 April 2021

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Learn to code with ikhomkodes')
# root.iconbitmap('/home/ikhom/PycharmProjects/tkinterGUI/DiUVXIFVQAE_ePs.jpg')

# root.filename = filedialog.askopenfilename(initialdir="/tkinterGUI/images", title="Select A File",
#                                            filetypes=(("png files", "*.png"), ("all files", "*.*")))


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/tkinterGUI/images", title="Select A File",
                                               filetypes=(("png files", "*.png"),
                                                          ("all files", "*.*"),
                                                          ("jpg files", "*.jpg"))
                                               )

    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text='Open File', command=open).pack()

mainloop()
