from tkinter import *
root=Tk()
root.title("Text Counter")
root.geometry("500x500")
root.config(bg="grey")


def text(): 
    input_text = en.get()  
    char_count = len(input_text)
    
    vowels="aeiouAEIOU"
    vowel_count = sum(1 for char in input_text if char in vowels)
    result.config(text=f"Character Count: {char_count} and Vowel Count: {vowel_count}") 

F1=Frame(root,bg="orange")
F1.pack(side="top",fill="x")





Label(F1,text="TEXT COUNT",fg="white",bg="orange", font="arial 20").pack()
Label(root,text="Enter your text",fg="white",bg="grey" ,font="aerial 15",pady=20).pack()

en = Entry(root, font="Arial 14")
en.pack(pady=10)

Button(root, text="Count text", command=text, font="Arial 15").pack(pady=10)
result = Label(root, text="", font="Arial 15", bg="grey")
result.pack(pady=10)

root.mainloop()
