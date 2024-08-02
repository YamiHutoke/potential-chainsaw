from tkinter import *
root=Tk()
root.geometry('500x500')
root.config(bg="white")


#Vertical
F1=Frame(root,bg="orange")
F1.pack(side="top",fill="x")
#Horizontal
F2=Frame(root,bg="lightgrey")
F2.pack(side="left",fill="y")



Label(F1,text="TEXT TOOL",fg="white",bg="orange", font="arial 20").pack()
Button(F2,text="Text to Speech",fg="black",bg="yellow",font="bold 15",width="20" ).pack()
Button(F2,text="Spelling Checker",fg="black",bg="yellow",font="bold 15",width="20").pack()
Button(F2,text="Textcase Convertor",fg="black",bg="yellow",font="bold 15",width="20").pack()
Button(F2,text="Text Count",fg="black",bg="yellow",font="bold 15",width="20").pack()
Button(F2,text="Email Extract",fg="black",bg="yellow",font="bold 15",width="20").pack()
Button(F2,text="URL Extract",fg="black",bg="yellow",font="bold 15",width="20").pack()
Button(F2,text="Synonym",fg="black",bg="yellow",font="bold 15",width="20").pack()
Button(F2,text="Antonym",fg="black",bg="yellow",font="bold 15",width="20").pack()
Button(F2,text="Logout",fg="white",bg="orange",font="bold 15",width="20").pack()
Label(root, text="WELCOME TO TEXT TOOL", font="Arial 16", fg="orange", pady=300).pack()
root.mainloop()
