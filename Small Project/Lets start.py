from tkinter import *

root = Tk()
root.geometry('500x500')
root.config(bg="white")


def f1():
    import Reg

# Title and start
F1 = Frame(root, bg="lightgrey")
F1.pack(side="top", fill="x")

F2 = Frame(root, bg="lightgrey")
F2.pack(side="top", fill="both", expand=True)

Label(F1, text="TEXT TOOL", fg="white", bg="orange", font="arial 20").pack()

Button(F2, text="Let's Start", fg="black", bg="yellow", font="bold 15", padx=20, pady=20, command=f1).pack(expand=True)

root.mainloop()
