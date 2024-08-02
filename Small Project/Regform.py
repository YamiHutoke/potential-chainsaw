from tkinter import *
root=Tk()
root.geometry('500x500')
root.config(bg="white")
import sqlite3
#Grid
def F1():
    con=sqlite3.connect('user.db')
    sq1="Create table if not exists reg(name variable(34),email variable(100),password variable(60))"
    con.execute(sq1)

    sq2="insert into reg(name,email,password) values(?,?,?)"
    data=(nm.get(),em.get(),pw.get())
    con.execute(sq2,data)
    con.commit()
    con.close()
#----------------------------------------------------------------------#    
    print(nm.get(), em.get(), pw.get())
nm=StringVar()
em=StringVar()
pw=StringVar()


F2=Frame(root,bg="orange")
F2.grid(row=0,columnspan=2,pady=20)



Label(F2,text="Registration Form",fg="white",bg="orange", font="arial 20").pack(pady=10)
Label(root,text="Name", font="arial 15").grid(row=1,column=0,padx=20, pady=10)
Entry(root, textvariable=nm, font="arial 15").grid(row=1,column=1,padx=20, pady=10)
Label(root,text="Email", font="arial 15").grid(row=2,column=0,padx=20, pady=10)
Entry(root, textvariable=em, font="arial 15").grid(row=2,column=1,padx=20, pady=10)
Label(root,text="Password", font="arial 15").grid(row=3,column=0,padx=20, pady=10)
Entry(root, textvariable=pw, font="arial 15").grid(row=3,column=1,padx=20, pady=10)
Label(root,text="Confirm Password", font="arial 15").grid(row=4,column=0,padx=20, pady=10)
Entry(root, textvariable=pw, font="arial 15").grid(row=4,column=1,padx=20, pady=10)
Button(root,text="Submit",fg="black", bg="yellow", font="bold 15",command=F1).grid(row=5,columnspan=2, pady=20)
root.mainloop()
