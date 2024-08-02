#Color picker (user can write"Colorchooser" as sometimes it shows error with colorpicker.

from tkinter import *
from tkinter import colorchooser

root=Tk()
root.geometry('400x400')
root.config(bg="grey")

def f1():
    x=colorchooser.askcolor(title="Select the desired color")
    root.config(bg=x[1])

Button(root,text="Select",command=f1).pack()

root.mainloop()

#-------------------------------------------------------------#

