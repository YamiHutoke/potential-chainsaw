from tkinter import *
root=Tk()
root.geometry('500x500')
root.config(bg="white")
import sqlite3

#Grid
def F1():
    match=False
    con=sqlite3.connect('user.db')
    sql="select * from reg"
    res=con.execute(sql)
    for i in res:
        if str(i[1])==str(em.get()) and str( i[2])== str(pw.get()):
            match=True
    if match==True:
        print("User sucessfully login")
    else:
        print("Invalid Info")
    print(em.get(), pw.get())
em=StringVar()
pw=StringVar()


#Title
F2=Frame(root,bg="orange")
F2.grid(row=0,columnspan=2,pady=20)
#Main
Label(F2,text="Login",fg="white",bg="orange", font="arial 20").pack(pady=10)

Label(root,text="Email", font="arial 13").grid(row=1,column=0,padx=20, pady=10)
Entry(root, textvariable=em, font="arial 13").grid(row=1,column=1,padx=20, pady=10)

Label(root,text="Password", font="arial 13").grid(row=2,column=0,padx=20, pady=10)
Entry(root, textvariable=pw, font="arial 13").grid(row=2,column=1,padx=20, pady=10)
Button(root,text="Submit",fg="black", bg="yellow", font="bold 15",command=F1).grid(row=3,columnspan=2, pady=20)
root.mainloop()
