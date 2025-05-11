import tkinter as tk
from tkinter import messagebox, ttk
import requests
from PIL import Image, ImageTk

# Function to create a gradient background
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

# Function to get weather data based on city or pin code
def get_weather_data(location, api_key, is_pin_code):
    if is_pin_code:
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={location},us&appid={api_key}&units=metric"
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to update the weather information on the GUI
def update_weather_info():
    location = location_entry.get()
    is_pin_code = pin_code_var.get()
    
    if location == "":
        messagebox.showerror("Input Error", "Please enter a city name or PIN code.")
        return
    
    api_key = "8efa5db1d843659b2030ef7d9db37fce"
    
    weather_data = get_weather_data(location, api_key, is_pin_code)
    
    if weather_data:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']
        icon_code = weather_data['weather'][0]['icon']
        
        weather_info_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWeather: {description}\nWind Speed: {wind_speed} m/s")
        
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
        icon_image = Image.open(requests.get(icon_url, stream=True).raw)
        icon_image = icon_image.resize((50, 50))
        icon_photo = ImageTk.PhotoImage(icon_image)
        weather_icon_label.config(image=icon_photo)
        weather_icon_label.image = icon_photo
    else:
        messagebox.showerror("Error", f"Could not retrieve weather data for {location}. Please check the input and try again.")

# Main window setup
app = tk.Tk()
app.title("Weather App")
app.geometry("480x530")
app.resizable(False, False)

# Background gradient
bg_canvas = tk.Canvas(app, width=480, height=530, highlightthickness=0)
bg_canvas.place(x=0, y=0)
_create_gradient(bg_canvas, 480, 530, "#008080", "#004d4d")  # Teal gradient

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

# Container frame for widgets
frame = tk.Frame(app, bg="#004d4d")
frame.place(x=30, y=30, width=420, height=470)

# Widgets
location_label = ttk.Label(frame, text="Enter PIN Code (USA) or City Name:", anchor='w')
location_label.pack(pady=(20, 8), anchor='w')

location_entry = ttk.Entry(frame, justify='center')
location_entry.pack(fill='x', pady=(0, 20))

pin_code_var = tk.BooleanVar()
pin_code_checkbox = ttk.Checkbutton(frame, text="Use PIN Code (USA)", variable=pin_code_var)
pin_code_checkbox.pack(anchor='w', pady=8)

get_weather_button = ttk.Button(frame, text="Get Weather", command=update_weather_info)
get_weather_button.pack(pady=22, ipadx=15)

weather_info_label = ttk.Label(frame, text="", anchor='w')
weather_info_label.pack(pady=(0, 10), anchor='w')

weather_icon_label = tk.Label(frame)
weather_icon_label.pack(pady=10)

# Run the application
app.mainloop()
