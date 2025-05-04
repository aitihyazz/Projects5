import tkinter as tk
import random

def play(choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)

    if choice == computer_choice:
        result = "It's a tie!"
    elif (choice == 'Rock' and computer_choice == 'Scissors') or \
         (choice == 'Paper' and computer_choice == 'Rock') or \
         (choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "You lose!"

    result_label.config(text=f"You chose {choice}\nComputer chose {computer_choice}\n{result}")

app = tk.Tk()
app.title("Rock Paper Scissors Game")
app.geometry("300x300")

label = tk.Label(app, text="Choose Rock, Paper or Scissors", font=('Arial', 12))
label.pack(pady=10)

button_frame = tk.Frame(app)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play('Rock'))
paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play('Paper'))
scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play('Scissors'))

rock_button.grid(row=0, column=0, padx=5)
paper_button.grid(row=0, column=1, padx=5)
scissors_button.grid(row=0, column=2, padx=5)

result_label = tk.Label(app, text="", font=('Arial', 12), fg='blue')
result_label.pack(pady=20)

app.mainloop()
