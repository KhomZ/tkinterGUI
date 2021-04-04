# Using Icons, Images, and Exit Buttons

from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to code with ikhomkodes")
# root.iconbitmap(r'@/home/ikhom/PycharmProjects/tkinterGUI/hnet.com-image.ico')

# img = PhotoImage(file='hnet.com-image.ico')

# root.tk.call('wm', 'iconbitmap', root._w, img)

# root.tk.call('wm', 'iconphoto', root._w, img)


my_img3 = ImageTk.PhotoImage(Image.open("DiUVXIFVQAE_ePs.jpg"))
my_img1 = ImageTk.PhotoImage(Image.open("images/ikhom1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/ikhom2.png"))

image_list = [my_img1, my_img2, my_img3]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)
# my_label.pack()


def forward(image_no):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_no - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_no + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_no - 1))

    if image_no == 3:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back():
    return


button_back = Button(root, text="<<", command=back)
button_quit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))


button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
# button_quit.pack()

root.mainloop()
