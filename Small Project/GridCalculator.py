from tkinter import *
import math
root=Tk()

root.config(bg="grey")
def f1(n):
    global data
    data=data+n
    s1.set(data)

def f2(n):
    global data
    data=c
    s1.set(c)

def f3(n):
    global data
    equal=eval(data)
    s1.set(equal)
def f4(n):
    global data
    sqr=math.sqrt(int(data))
    s1.set(sqr)

def f5(n):
    global data
    data = data[:-1]
    s1.set(data)

def f6(n):
    global data
    fact=math.factorial(int(data))
    s1.set(fact)
    

c=" "
data=""
s1=StringVar()

Entry(root,text="",bg="white", width="25",textvariable=s1).grid(row=0,columnspan=4)

Button(root,text="7",bg="black",fg="white", font="10", padx=5, command=lambda:f1('7')).grid(row=1,column=0)
Button(root,text="8",bg="black",fg="white", font="10", padx=5, command=lambda:f1('8')).grid(row=1,column=1)
Button(root,text="9",bg="black",fg="white", font="10", padx=5, command=lambda:f1('9')).grid(row=1,column=2)
Button(root,text="+",bg="orange", font="10", padx=5, command=lambda:f1('+')).grid(row=1,column=3)

Button(root,text="4",bg="black",fg="white", font="10", padx=5, command=lambda:f1('4')).grid(row=2,column=0)
Button(root,text="5",bg="black",fg="white", font="10", padx=5, command=lambda:f1('5')).grid(row=2,column=1)
Button(root,text="6",bg="black",fg="white", font="10", padx=5, command=lambda:f1('6')).grid(row=2,column=2)
Button(root,text="-",bg="orange", font="10", padx=5, command=lambda:f1('-')).grid(row=2,column=3)

Button(root,text="1",bg="black",fg="white", font="10", padx=5, command=lambda:f1('1')).grid(row=3,column=0)
Button(root,text="2",bg="black",fg="white", font="10", padx=5, command=lambda:f1('2')).grid(row=3,column=1)
Button(root,text="3",bg="black",fg="white", font="10", padx=5, command=lambda:f1('3')).grid(row=3,column=2)
Button(root,text="*",bg="orange", font="10", padx=5, command=lambda:f1('*')).grid(row=3,column=3)

Button(root,text="C",bg="black",fg="white", font="10", padx=5, command=lambda:f2('C')).grid(row=4,column=0)
Button(root,text="0",bg="black",fg="white", font="10", padx=5, command=lambda:f1('0')).grid(row=4,column=1)
Button(root,text="=",bg="black",fg="white", font="10", padx=5, command=lambda:f3('=')).grid(row=4,column=2)
Button(root,text="/",bg="orange", font="10", padx=5, command=lambda:f1('/')).grid(row=4,column=3)
Button(root,text="/",bg="orange", font="10", padx=5, command=lambda:f4('/')).grid(row=5,column=0)
Button(root,text="^",bg="orange", font="10", padx=5, command=lambda:f1('**')).grid(row=5,column=1)
Button(root,text="!",bg="orange", font="10", padx=5, command=lambda:f6('!')).grid(row=5,column=2)
Button(root,text="<-",bg="orange", font="10", padx=5, command=lambda:f5('<-')).grid(row=5,column=3)
root.mainloop()
