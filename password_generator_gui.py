import tkinter as tk
from tkinter import messagebox, ttk
import random
import string

def _create_gradient(canvas, width, height, start_color, end_color):
    r1, g1, b1 = canvas.winfo_rgb(start_color)
    r2, g2, b2 = canvas.winfo_rgb(end_color)
    r_ratio = float(r2 - r1) / height
    g_ratio = float(g2 - g1) / height
    b_ratio = float(b2 - b1) / height

    for i in range(height):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = f'#{nr//256:02x}{ng//256:02x}{nb//256:02x}'
        canvas.create_line(0, i, width, i, fill=color)

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_set = ''
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        password_entry.config(state='normal')
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state='readonly')
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def copy_to_clipboard():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Warning", "No password to copy.")
        return
    app.clipboard_clear()
    app.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Main window setup
app = tk.Tk()
app.title("Random Password Generator")
app.geometry("480x530")  # Increased height to fit all content
app.resizable(False, False)

# Background gradient
bg_canvas = tk.Canvas(app, width=480, height=530, highlightthickness=0)
bg_canvas.place(x=0, y=0)
_create_gradient(bg_canvas, 480, 530, "#008080", "#004d4d")  # teal gradient

# Style configuration
style = ttk.Style()
style.theme_use('clam')

# Entry style
style.configure('TEntry',
                foreground="#004d4d",
                fieldbackground="#b2dfdb",
                bordercolor="#00796b",
                lightcolor="#00796b",
                padding=8,
                relief="flat",
                font=('Segoe UI', 14))

# Button style
style.configure('TButton',
                background="#00796b",
                foreground="white",
                font=('Segoe UI Semibold', 14),
                padding=10)
style.map('TButton',
          background=[('active', '#004d40'), ('!disabled', '#00695c')],
          foreground=[('active', 'white'), ('!disabled', 'white')])

# Label style
style.configure('TLabel',
                background="#004d4d",
                foreground="white",
                font=('Segoe UI', 16))

# Checkbutton style
style.configure('TCheckbutton',
                background="#004d4d",
                foreground="white",
                font=('Segoe UI', 14))
style.map('TCheckbutton',
          background=[('active', '#004d40'), ('!disabled', '#004d4d')],
          foreground=[('active', 'white'), ('!disabled', 'white')])

# Container frame for widgets
frame = tk.Frame(app, bg="#004d4d")
frame.place(x=30, y=30, width=420, height=470)  # Adjusted frame size for new height

# Widgets
length_label = ttk.Label(frame, text="Password Length:")
length_label.pack(pady=(20, 8), anchor='w')

length_entry = ttk.Entry(frame, justify='center')
length_entry.pack(fill='x', pady=(0, 20))

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

letters_check = ttk.Checkbutton(frame, text="Include Letters", variable=letters_var)
letters_check.pack(anchor='w', pady=2)

numbers_check = ttk.Checkbutton(frame, text="Include Numbers", variable=numbers_var)
numbers_check.pack(anchor='w', pady=2)

symbols_check = ttk.Checkbutton(frame, text="Include Symbols", variable=symbols_var)
symbols_check.pack(anchor='w', pady=10)

generate_button = ttk.Button(frame, text="Generate Password", command=on_generate)
generate_button.pack(pady=22, ipadx=15)

password_label = ttk.Label(frame, text="Generated Password:")
password_label.pack(pady=(0, 10), anchor='w')

password_entry = ttk.Entry(frame, justify='center', font=('Segoe UI', 20))
password_entry.pack(fill='x')
password_entry.config(state='readonly')

copy_button = ttk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=18, ipadx=15)

app.mainloop()
