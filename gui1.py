from pathlib import Path
from subprocess import run
from tkinter import Toplevel, Label, Button
import webbrowser
from tkinter import simpledialog
import pandas as pd
import os

# from tkinter import *

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame1")

def open_gui2():
    run(["python", str(Path(r".\gui2.py"))])

def open_gui3():
    run(["python", str(Path(r".\gui3.py"))])

def open_url():
    url = "https://coek.dypgroup.edu.in/academics/syllabus/" 
    webbrowser.open(url)

def open_gui4():
    run(["python", str(Path(r".\Genetic_Algo.py"))])

def open_student():
    run(["python", str(Path(r".\Student.py"))])
    


def check_password(entry_widget):
    # Replace 'your_password' with the actual password you want to use
    global GetPass
    correct_password = 1234
    entered_password = int(entry_widget.get())
    
    
    if entered_password == correct_password:
        open_gui2()
    elif (entered_password > 2100 and entered_password < 2161) or (entered_password > 2200 and entered_password < 2261) or (entered_password > 3100 and entered_password < 3161) or (entered_password > 3200 and entered_password < 3261) or (entered_password > 4100 and entered_password < 4161) or (entered_password > 4200 and entered_password < 4261):
        with open(r'.\getpass.txt', 'w') as file:
            file.write(str(entered_password))
        open_student()
    else:
        print("Incorrect password")

def fetchpass():
    return GetPass

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Function to toggle fullscreen using f5 and escape button
def toggle_fullscreen(event=None):
    global fullscreen_state
    if event and event.keysym == "F5":
        window.attributes("-fullscreen", True)
        fullscreen_state = True

    elif event and event.keysym == "Escape":
        window.attributes("-fullscreen", False)
        fullscreen_state = False




window = Tk()
# Get the screen width and height

window.title("Automated Timetable Generator")
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
    bg = "#ffffff",
    height = 790,
    width = 1532,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.pack(fill="both", expand=True)

# 1536 , 864

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    760,
    400,
    image=image_image_1
)

canvas.create_rectangle(
    0.0,
    150.0,
    1536.0,
    142.0,
    fill="#FFFFFF",
    outline="")

# 1536 , 129

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    760,
    75,
    image=image_image_2
)

# TimeTable Button
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=check_password,
    relief="flat"
)
button_1.place(
    x=100.0,
    y=190.0,
    width=226,
    height=38
)

# Submit Button
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: check_password(entry_2),
    relief="flat"
)
button_2.place(
    x=350.0,
    y=568.0,
    width=226,
    height=38
)

# Dashboard Button
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui4,
    relief="flat"
)
button_3.place(
    x=650.0,
    y=190.0,
    width=226,
    height=38
)

canvas.create_text(
    150.0,
    330.0,
    anchor="nw",
    text="    Name : ",
    fill="#FFFFFF",
    font=("JuliusSansOne Regular", 25 * -1)
)

# Name's Entry
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font= 19
)
entry_1.place(
    x=350,
    y=326,
    width=395.0,
    height=34.7
)

# Password Text
canvas.create_text(
    150.0,
    440.0,
    anchor="nw",
    text="    Password : ",
    fill="#FFFFFF",
    font=("JuliusSansOne Regular", 25 * -1)
)

# Password Entry
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font= 19,
    show="*"  
)
entry_2.place(
    x=350,
    y=435,
    width=395.0,
    height=34.7
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1123.0,
    431.0,
    image=image_image_3
)

# Syllabus Button
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=open_url,
    relief="flat"
)
button_4.place(
    x=1200.0,
    y=190.0,
    width=226,
    height=38
)

window.resizable(True, True)
window.mainloop()
