import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt

# Function to create vertical gradient on canvas
def _create_gradient(canvas, width, height, start_color, end_color):
    # Interpolate RGB colors and draw rectangles line by line
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

# Function to calculate BMI
def calculate_bmi(weight, height):
    try:
        # Debugging: print weight and height
        print(f"Debug: weight={weight}, height={height}")
        
        if height <= 0:
            raise ValueError("Height must be greater than zero.")
        if weight <= 0:
            raise ValueError("Weight must be greater than zero.")
        
        bmi = round(weight / (height ** 2), 2)
        print(f"Debug: Calculated BMI = {bmi}")
        return bmi
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
        return None

# Function to classify BMI
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Show BMI trend graph
def show_bmi_trend():
    if not bmi_values:
        messagebox.showinfo("No Data", "No BMI data available to show a trend.")
        return
    plt.plot(range(1, len(bmi_values)+1), bmi_values, marker='o', linestyle='-', color='#1976d2')
    plt.title('BMI Trend Over Time')
    plt.xlabel('Entry Number')
    plt.ylabel('BMI')
    plt.xticks(range(1, len(bmi_values)+1))
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Calculate and store BMI
def calculate_and_store_bmi():
    weight = weight_entry.get()
    height = height_entry.get()
    print(f"Debug: weight_entry={weight}, height_entry={height}")

    try:
        weight = float(weight)
        height = float(height)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for weight and height.")
        return

    print(f"Debug: After conversion weight={weight}, height={height}")

    if weight <= 0 or height <= 0:
        messagebox.showerror("Input Error", "Please enter positive values for weight and height.")
        return

    bmi = calculate_bmi(weight, height)
    if bmi is not None:
        bmi_values.append(bmi)
        bmi_category = classify_bmi(bmi)
        # Update result label with color-coded classification
        color_map = {
            "Underweight": "#64b5f6",  # light blue
            "Normal weight": "#388e3c",  # green
            "Overweight": "#ffb300",    # amber
            "Obesity": "#d32f2f"        # red
        }
        result_label.config(text=f"BMI: {bmi} ({bmi_category})", foreground=color_map.get(bmi_category, "black"))
        results_listbox.insert(tk.END, f"Weight: {weight}kg, Height: {height}m, BMI: {bmi} ({bmi_category})")

# Main window setup
app = tk.Tk()
app.title("BMI Calculator")
app.geometry("360x550")
app.resizable(False, False)

# Create canvas for gradient background
bg_canvas = tk.Canvas(app, width=360, height=550, highlightthickness=0)
bg_canvas.place(x=0, y=0)
_create_gradient(bg_canvas, 360, 550, "#0d47a1", "#1976d2")  # blue gradient

# Style configuration
style = ttk.Style()
style.theme_use('clam')

# Configure ttk.Entry style
style.configure('TEntry',
                foreground="#212121",
                fieldbackground="#bbdefb",
                bordercolor="#64b5f6",
                lightcolor="#64b5f6",
                padding=6,
                relief="flat",
                font=('Segoe UI', 12))

# Configure ttk.Button style with rounded corners simulation, recolored and hovered
style.configure('TButton',
                background="#1565c0",
                foreground="white",
                font=('Segoe UI Semibold', 12),
                padding=8)
style.map('TButton',
          background=[('active', '#0d47a1'), ('!disabled', '#1976d2')],
          foreground=[('active', 'white'), ('!disabled', 'white')])

# Configure ttk.Label style
style.configure('TLabel',
                background="#1976d2",
                foreground="white",
                font=('Segoe UI', 13))

# Frame to hold widgets with transparent bg via canvas
frame = tk.Frame(app, bg="#1976d2")
frame.place(x=20, y=20, width=320, height=510)

bmi_values = []

weight_label = ttk.Label(frame, text="Enter weight (kg):")
weight_label.pack(pady=(20, 5))

weight_entry = ttk.Entry(frame, justify='center')
weight_entry.pack(pady=(0, 20), fill='x')

height_label = ttk.Label(frame, text="Enter height (m):")
height_label.pack(pady=(0,5))

height_entry = ttk.Entry(frame, justify='center')
height_entry.pack(pady=(0, 20), fill='x')

calculate_button = ttk.Button(frame, text="Calculate BMI", command=calculate_and_store_bmi)
calculate_button.pack(pady=(0, 20), ipadx=10)

result_label = ttk.Label(frame, text="BMI: ")
result_label.pack(pady=(0, 20))

trend_button = ttk.Button(frame, text="Show BMI Trend", command=show_bmi_trend)
trend_button.pack(pady=(0, 20), ipadx=10)

# Listbox with scrollbar for history
listbox_frame = tk.Frame(frame)
listbox_frame.pack(pady=(0,20), fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

results_listbox = tk.Listbox(listbox_frame, yscrollcommand=scrollbar.set, font=('Segoe UI', 10))
results_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=results_listbox.yview)

app.mainloop()

