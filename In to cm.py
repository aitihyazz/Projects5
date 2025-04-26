from tkinter import *
root=Tk()
root.geometry("400x400")
def converter():
    value = entry.get()
    if value.replace('.', '', 1).isdigit():
        inches = float(value) / 2.54
        label.config(text = str(inches) + " inches")
    else:
        label.config(text="Enter a valid number!")
entry = Entry(root)
entry.place(x=100, y=50)

button = Button(root, text="Calculate", command=converter)
button.place(x=100, y=100)

label = Label(root, text="")
label.place(x=100, y=150)

root.mainloop()