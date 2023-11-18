import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    length = int(length_var.get())

    contain_numbers = numbers_var.get()
    contain_symbols = symbols_var.get()

    characters = string.ascii_letters
    if contain_numbers:
        characters += string.digits
    if contain_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create and place widgets
length_label = ttk.Label(window, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_var = tk.StringVar()
length_entry = ttk.Entry(window, textvariable=length_var)
length_entry.grid(row=0, column=1, padx=10, pady=10)

numbers_var = tk.BooleanVar()
numbers_checkbox = ttk.Checkbutton(window, text="Include Numbers", variable=numbers_var)
numbers_checkbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

symbols_var = tk.BooleanVar()
symbols_checkbox = ttk.Checkbutton(window, text="Include Symbols", variable=symbols_var)
symbols_checkbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

generate_button = ttk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
result_label = ttk.Label(window, textvariable=result_var, font=('Helvetica', 12))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the main loop
window.mainloop()