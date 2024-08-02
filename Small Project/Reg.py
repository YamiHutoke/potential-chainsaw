from tkinter import *
root=Tk()
root.geometry('500x500')
root.config(bg="white")

def f1():
    import Regform

def f2():
    import Login
#Vertical
F1=Frame(root,bg="orange")
F1.pack(side="top",fill="x")

#Buttons#
F2 = Frame(root, bg="lightgrey")
F2.pack(side="top", fill="both", expand=True)

Label(F1,text="TEXT TOOL",fg="white",bg="orange", font="arial 20").pack()


Button(F2, text="Register", fg="black", bg="yellow", font="bold 15", padx=20, pady=20,command=f1).pack(expand=True)
Button(F2, text="Log in", fg="black", bg="yellow", font="bold 15", padx=30, pady=20,command=f2).pack(expand=True)
