from tkinter import *
import pyqrcode
import png
from pyqrcode import QRCode

root = Tk()
root.title("Text Counter")
root.geometry("500x500")
root.config(bg="grey")


def QR():
    text = en.get()
    qrcode = pyqrcode.create(text)
    file = "myqr.png"
    qrcode.png(file, scale=8)
    print("done")

#Frame
F1 = Frame(root, bg="orange")
F1.pack(side="top", fill="x")

# Titles
Label(F1, text="QR GENERATOR", fg="white", bg="orange", font="Arial 20").pack()
Label(root, text="Enter your URL", fg="white", bg="grey", font="Arial 15", pady=20).pack()

en = Entry(root, font="Arial 14")
en.pack(pady=10)

#Button
Button(root, text="Generate a QR Code", font="Arial 15", command=QR).pack(pady=10)


root.mainloop()
