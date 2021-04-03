# Adding Frames to Your Program
# Developer: Khom
# @ikhomkodes
# Date: Friday, 2 April 2021

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Coding with iKhom')

frame = LabelFrame(root, text="This is my Frame...", padx=50, pady=50)
frame.pack(padx=100, pady=100)

b = Button(frame, text="Don't Click here!!")
# b.pack()
b2 = Button(frame, text="... or here!")
b.grid(row=0, column=0)
b2.grid(row=1,column=0)

root.mainloop()
