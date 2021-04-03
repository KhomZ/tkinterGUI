from tkinter import *

root = Tk()
root.title('Icon Test')
root.iconbitmap('hnet.com-image.ico')

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
