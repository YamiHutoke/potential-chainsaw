from tkinter import *
import datetime

def age():
    current = datetime.datetime.now()
    birth = datetime.datetime.strptime(en.get(), "%d-%m-%Y")
    age = current.year - birth.year - ((current.month, current.day) < (birth.month, birth.day))
    result.config(text=f"You are {age} years old.")

root = Tk()
root.title("Age Calculator")
root.geometry("500x500")
root.config(bg="grey")

Label(root, text="Age Calculator", font="Arial 20", fg="orange", bg="grey", pady=20).pack()

en = Entry(root, font="Arial 14")
en.pack(pady=10)
en.insert(0, "DD-MM-YYYY")

Button(root, text="Calculate Age", command=age, font="Arial 15").pack(pady=10)

result = Label(root, text="", font="Arial 15", bg="grey")
result.pack(pady=10)

root.mainloop()
