from tkinter import *

window = Tk()
window.geometry("400x400")
window.title("Interest")

def interest():
    try:
        p = float(pentry.get())
        r = float(rentry.get())
        t = float(tentry.get())

        si = (p * r * t) / 100  
        amount = p * (1 + r/100) ** t 
        ci = amount - p  

        result_label.config(text=f"Simple Interest: {si:.2f}\nCompound Interest: {ci:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")

Label(window, text="Principal (P):", font=("Arial", 12)).pack(pady=5)
pentry = Entry(window)
pentry.pack(pady=5)

Label(window, text="Rate of Interest (R%):", font=("Arial", 12)).pack(pady=5)
rentry = Entry(window)
rentry.pack(pady=5)

Label(window, text="Time (T years):", font=("Arial", 12)).pack(pady=5)
tentry = Entry(window)
tentry.pack(pady=5)

Button(window, text="Calculate Interest", command=interest, font=("Arial", 12)).pack(pady=20)

result_label = Label(window, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

window.mainloop()
