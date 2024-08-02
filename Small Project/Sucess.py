from tkinter import *
root=Tk()
root.geometry('500x500')
root.config(bg="white")

F1=Frame(root,bg="orange")
F1.grid(row=0,columnspan=2,pady=20)

def F2():
    import GridCalculator

def F3():
    import GUIcolorpicker

def F4():
    import Darklighttheme

def F5():
    import AgeCalculator

def F6():
    import DigitalClock

def F7():
    import TextCount

def F8():
    import TextTransform

def F9():
    import QRGenerator

Label(F1,text="Sucessful Login",fg="white",bg="orange", font="arial 20").pack(pady=10)

Button(root,text="Calculator",fg="black", bg="yellow", font="bold 15",width="20", command=F2).grid(row=1,column=0)
Button(root,text="Digital Clock",fg="black",bg="yellow",font="bold 15",width="20",command=F6).grid(row=1,column=1)
Button(root,text="color chooser",fg="black", bg="yellow", font="bold 15",width="20",command=F3).grid(row=2,column=0)
Button(root,text="theme",fg="black", bg="yellow", font="bold 15",width="20",command=F4).grid(row=2,column=1)
Button(root,text="QR generator",fg="black", bg="yellow", font="bold 15",width="20",command=F9).grid(row=3,column=0)
Button(root,text="Text Transform",fg="black", bg="yellow", font="bold 15",width="20",command=F8).grid(row=3,column=1)
Button(root,text="Text Count",fg="black", bg="yellow", font="bold 15",width="20",command=F7).grid(row=4,column=0)
Button(root,text="Age Calculator",fg="black", bg="yellow", font="bold 15",width="20",command=F5).grid(row=4,column=1)

