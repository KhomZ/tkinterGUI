# Creating Input Fields

from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="red", fg="blue")
e.pack()
e.insert(0, "Enter Your Name: ")


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Enter Your Name: ", command=myClick)
myButton.pack()

root.mainloop()

# Some common colors
# S.N.  Color     Decimal(Red,Green,Blue)     Hexadecimal (#RRGGBB)
# 1.    Black            (0,   0,   0)                    (#000000)
# 2.    White            (255, 255, 255)                  (#FFFFFF)
# 3.    Red              (255, 0,   0)                    (#FF0000)
# 4.    Green            (0,   255, 0)                    (#00FF00)
# 5.    Blue             (0,    0,  255)                  (#0000FF)
# 6.    Yellow           (255,  255,  0)                  (#FFFF00)
# 7.    Cyan             (0,    255,  255)                (#00FFFF)
# 8.    Magenta          (255,  0,    255)                (#FF00FF)

