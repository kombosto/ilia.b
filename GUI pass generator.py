import tkinter as tk
from tkinter import ttk
import secrets
import string

def generate_password():
    length = length_var.get()
    chars = ""

    if letters_var.get():
        chars += string.ascii_letters
    if digits_var.get():
        chars += string.digits
    if symbols_var.get():
        chars += string.punctuation

    if not chars:
        password_var.set("Select at least one option")
        return

    password = ''.join(secrets.choice(chars) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())

# Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x300")
root.resizable(False, False)

# Variables
length_var = tk.IntVar(value=12)
letters_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()

# Widgets
ttk.Label(root, text="Password Length").pack(pady=5)
ttk.Spinbox(root, from_=6, to=64, textvariable=length_var, width=5).pack()

ttk.Checkbutton(root, text="Letters", variable=letters_var).pack()
ttk.Checkbutton(root, text="Digits", variable=digits_var).pack()
ttk.Checkbutton(root, text="Symbols", variable=symbols_var).pack()

ttk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

ttk.Entry(root, textvariable=password_var, width=30).pack(pady=5)
ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack()

root.mainloop()
