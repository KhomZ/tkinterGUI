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

my_img = ImageTk.PhotoImage(Image.open("DiUVXIFVQAE_ePs.jpg"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
