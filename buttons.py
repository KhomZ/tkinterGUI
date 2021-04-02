# Creating Buttons
# @author: ikhomkodes

from tkinter import *

root = Tk()

# myButton = Button(root, text="Click Me!")

# more options
# myButton = Button(root, text="Click Me!", state=DISABLED)    #disabling button click
# myButton = Button(root, text="Click Me!", padx=50, pady=50)  #resizing the button


def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!!")
    myLabel.pack()


myButton = Button(root, text="Click Me!", command=myClick, fg="cyan", bg="#000000")
myButton.pack()

root.mainloop()
