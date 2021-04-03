# Adding a status bar
# Developer: Khom
# @ikhomkodes
# Date: Saturday, 3 Apr 2021


from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('ikhomkodes Image Viewer')
# root.iconbitmap("/home/ikhom/PycharmProjects/tkinterGUI/DiUVXIFVQAE_ePs.jpg")

my_img1 = ImageTk.PhotoImage(Image.open("images/khom1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/khom2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/khom3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/khom4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/khom5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("images/khom6.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("images/IMG_0478.JPG"))


image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
