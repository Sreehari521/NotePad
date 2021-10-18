from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("500x600")

def save_file():
    open_file = filedialog.asksaveasfile(mode="w", defaultextension=".*")
    if open_file is None:
        return
    text = str(entry.get(1.0, END))
    open_file.write(text)
    open_file.close()

def clear():
    entry.delete(1.0, END)

def open_file():
    file = filedialog.askopenfile(mode="r")
    if file is not None:
        content = file.read()
    entry.insert(INSERT, content)

b1 = Button(root, text="save", command=save_file, font="sans-serif")
b1.place(x=10, y=10)

b1 = Button(root, text="clear", command=clear, font="sans-serif")
b1.place(x=70, y=10)

b1 = Button(root, text="open", command=open_file, font="sans-serif")
b1.place(x=130, y=10)

entry = Text(root, height=33, width=58, wrap=WORD)
entry.place(x=10, y=50)

root.mainloop()