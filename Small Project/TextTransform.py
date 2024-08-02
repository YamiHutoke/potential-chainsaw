from tkinter import *

root = Tk()
root.geometry("500x500")
root.config(bg="lightgrey")

def Upper():
    a=en.get()
    res=a.upper()
    x.config(text=res)

def Lower():
    a=en.get()
    res=a.lower()
    x.config(text=res)

def Capitalize():
    a=en.get()
    res=a.capitalize()
    x.config(text=res)

def Swapcase():
    a=en.get()
    res=a.swapcase()
    x.config(text=res)

def Title():
    a=en.get()
    res=a.title()
    x.config(text=res)

F1 = Frame(root, bg="orange")
F1.grid(row=0, columnspan=3, pady=20)

F2 = Frame(root, bg="orange")
F2.grid(row=1, columnspan=4, pady=15)

Label(F1, text="TEXT TOOL", fg="white", bg="orange", font="arial 20").pack(pady=10)
Label(F2, text="Enter your text", fg="black", bg="orange", font="arial 15").pack(pady=20)

# Entry
en = Entry(root, font="Arial 14")
en.grid(row=2,columnspan=2,pady=10)

# Buttons
Button(root, text="Uppercase", fg="black", bg="orange", font="aerial 10", width="15",command=Upper).grid(row=3, column=0)
Button(root, text="Lowercase", fg="black", bg="orange", font="aerial 10", width="15",command=Lower).grid(row=3, column=1)
Button(root, text="Capital", fg="black", bg="orange", font="aerial 10", width="15",command=Capitalize).grid(row=3, column=2)
Button(root, text="SwapCase", fg="black", bg="orange", font="aerial 10", width="15",command=Swapcase).grid(row=4, column=0)
Button(root, text="Title", fg="black", bg="orange", font="aerial 10", width="15",command=Title).grid(row=4, column=1)

x=Label(root, )
x.grid(row=5, column=1)

root.mainloop()
