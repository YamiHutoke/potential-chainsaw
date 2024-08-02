from tkinter import *
root=Tk()
root.geometry('500x500')
root.config(bg="white")
#Now to make the dark and light theme.
#We keep the theme as Light by default.
mode="Light"

def btn():
    global mode
    if mode =="Light":
        root.config(bg="black")
        L1.config(bg="black",fg="white")
        b.config(text="Light Mode",bg="white", fg="black")
        mode="Dark"

    else:
        root.config(bg="white")
        L1.config(bg="white",fg="black")
        b.config(text="Dark Mode",bg="black", fg="white")
        mode="Light"

b=Button(root, text="Dark Mode", bg="black", fg="white", command=btn)
b.pack()

L1=Label(root,text="Dreadful Nights but I am still standing",bg="white")
L1.pack()
root.mainloop()
#1.Firstly we will make a button that can change the light theme to dark
#2.Then we can observe that the button is only changing it to dark but if the user wants it to work so that it can change back and fourth
#3.We will make a function which will make it so that theme works back and forth and also we will use global statement as we want the changes in the whole file
#4.and also we will use if statement.
