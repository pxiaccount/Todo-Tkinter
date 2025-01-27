from tkinter import *

root = Tk()
root.title("Todo")
root.geometry("500x600")

heading = Label(root, text="Todo", font=("TkDefaultFont", 32))
heading.pack()

text_input = Entry(root, font=("TkDefaultFont", 16))
text_input.pack()

todo_array = []

def add_todo():
    current = text_input.get()
    if current:
        todo_array.append(current)
        text_input.delete(0, END)
        todo()

def delete(i):
    todo_array.remove(i)
    todo()

def todo():
    for widget in root.winfo_children():
        if isinstance(widget, Label) and widget != heading:
            widget.destroy()
        elif isinstance(widget, Button):
            widget.destroy()
    for i in todo_array:
        label = Label(root, text=i)
        label.pack(pady=5)
        button = Button(root, text="Delete", command=lambda i=i: delete(i))
        button.pack()

text_input.bind("<Return>", lambda e: add_todo())

root.mainloop()