from pathlib import Path
from subprocess import run
import webbrowser
from tkinter import ttk
import sys
from tabulate import tabulate
import pandas as pd
import os
import tkinter as tk
from PIL import Image, ImageTk
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Button, Canvas ,Label ,PhotoImage, Text, Scrollbar, scrolledtext



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame2")

def open_gui4():
    run(["python", str(Path(r".\Second Year.py"))])

def open_studash():
    run(["python", str(Path(r".\Dashboard 2nd year A.py"))])

def open_url():
    url = "https://coek.dypgroup.edu.in/academics/syllabus/"  # Replace with your desired URL
    webbrowser.open(url)

def open_excel_sheet(excel_file_path):
    os.startfile(excel_file_path)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def place_image_on_frame(frame, image_path):
    # Open the image file
    image = Image.open(image_path)

    # Convert the image to a format compatible with tkinter
    tk_image = ImageTk.PhotoImage(image)

    # Create a label widget to display the image
    label = tk.Label(frame, image=tk_image)
    label.image = tk_image  # Keep a reference to prevent garbage collection

    # Place the label on the frame
    label.pack()
    
# Function to toggle fullscreen using f5 and escape button
def toggle_fullscreen(event=None):
    global fullscreen_state
    if event and event.keysym == "F5":
        window.attributes("-fullscreen", True)
        fullscreen_state = True

    elif event and event.keysym == "Escape":
        window.attributes("-fullscreen", False)
        fullscreen_state = False

# Load Excel file
excel_file = pd.ExcelFile(r".\Students_Data.xlsx")

# Define column names
column_names = ['Student Name', 'Password']

# Create an empty dictionary to store the mapping of passwords to students
password_student_mapping = {}

# Iterate through each sheet and read data into DataFrame
for sheet_name in excel_file.sheet_names:
    df = pd.read_excel(excel_file, sheet_name=sheet_name, names=column_names)
    # Iterate through each row in the DataFrame and populate the dictionary
    for index, row in df.iterrows():
        password_student_mapping[row['Password']] = (row['Student Name'], sheet_name)

password = ""
with open(r'.\getpass.txt', 'r') as file:
        password = int(file.read().strip())

student_name, sheet_name = password_student_mapping[password]

window = tk.Tk()

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window dimensions
window_width = int(screen_width * 0.8)  # 80% of the screen width
window_height = int(screen_height * 0.8)  # 80% of the screen height

# Calculate the position to center the window
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window dimensions to match the screen size
window.geometry(f"{screen_width}x{screen_height}")

# Bind the F5 key to toggle fullscreen
window.bind("<F5>", toggle_fullscreen)

# Bind the Escape key to exit fullscreen
window.bind("<Escape>", toggle_fullscreen)

window.configure(bg = "#2C4072")

window.pack_propagate(False)

canvas = Canvas(
    window,
    bg = "#2C4072",
    height = 789,
    width = 1530,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_url,
    relief="flat"
)
button_1.place(
    x=1075.0,
    y=111.0,
    width=211.63711547851562,
    height=34.0
)

canvas.create_rectangle(
    0.0,
    90.0,
    1530.0,
    85.0,
    fill="#FFFFFF",
    outline="")

text = canvas.create_text(765, 36, text="Welcome, ", font=("Arial", 30), anchor="center", fill= "white")
canvas.itemconfig(text, text=f"Welcome, {student_name}!")


button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=print("Button Clicked1"),
    relief="flat"
)
button_2.place(
    x=225.0,
    y=110.0,
    width=211.63711547851562,
    height=35.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_studash,
    relief="flat"
)
button_3.place(
    x=650.0,
    y=111.0,
    width=211.63711547851562,
    height=34.0
)

excel_frame = ttk.Frame(canvas)
excel_frame.place(x=100, y=180, width=1240, height=1080)

if password // 1000 == 2 :
    password = password % 1000
    if password // 100 == 1:
        place_image_on_frame(excel_frame,r".\2nd_Year_Division_1.png")
    else :
        place_image_on_frame(excel_frame,r".\2nd_Year_Division_2.png")
elif password // 1000 == 3 : 
    password = password % 1000
    if password // 100 == 1:
        place_image_on_frame(excel_frame,r".\3rd_Year_Division_1.png")
    else:
        place_image_on_frame(excel_frame,r".\3rd_Year_Division_2.png")


window.resizable(True, True)
window.mainloop()
