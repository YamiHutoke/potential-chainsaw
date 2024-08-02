#Now for the digital clock
from tkinter import *
from time import strftime

root=Tk()
root.config(bg="grey")
def clk():
    res=strftime("%d-%b-%Y %a %H:%M:%S %p")
    x.config(text=res)
    x.after(1000,clk)

x=Label(root,bg="black",fg="red",font="Arial,35")
x.pack()

clk()
root.mainloop()
