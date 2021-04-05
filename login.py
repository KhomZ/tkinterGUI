# >_ ikhomkodes
#
# @ikhomkodes
#
# Python Program for login page using Tkinter Package
# Date: Monday, 5 April 2021

from tkinter import *

root = Tk()   # create a GUI window


# Designing MainScreen, first, design main screen with Login & Register buttons
def main_screen():
    root.geometry("800x800")  # set the configuration of GUI window
    root.title("Login Page")  # set the title of GUI window


# create a Form Label
Label(text="Login Window with ikhomkodes", bg="green", width="30", height="2", font=("Calibri", 13)).pack()
Label(text="").pack()

# create a Login button
Button(text="Login", height="2", width="30").pack()
Label(text="").pack()

# create a Register button
Button(text="Register", height="2", width="30").pack()

root.mainloop()  # start the GUI

main_screen()   # call the main_account_screen() function
