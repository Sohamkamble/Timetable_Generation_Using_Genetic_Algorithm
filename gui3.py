from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import pandas as pd
from data import *
from subprocess import run
import webbrowser


# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame3")

def open_gui2():
    run(["python", str(Path(r".\gui2.py"))])

def open_gui3():
    run(["python", str(Path(r".\Dashboard 3rd year A.py"))])

def open_gui4():
    run(["python", str(Path(r".\Dashboard 2nd year A.py"))])

def open_gui5():
    run(["python", str(Path(r".\Dashboard 2nd year B.py"))])

def open_gui6():
    run(["python", str(Path(r".\Dashboard 3rd year B.py"))])

def open_url():
    url = "https://coek.dypgroup.edu.in/academics/syllabus/"  # Replace with your desired URL
    webbrowser.open(url)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("880x550")
window.configure(bg = "#2C4072")

window.title("Dashboard")
canvas = Canvas(
    window,
    bg = "#2C4072",
    height = 550,
    width = 880,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)


image_image_1 = PhotoImage(
    file=relative_to_assets("TY 3B.png"))
image_1 = canvas.create_image(
    130.0,
    350.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("TY 3A.png"))
image_2 = canvas.create_image(
    340.0,
    350.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("TY 2A.png"))
image_3 = canvas.create_image(
    550.0,
    350.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("TY 2B.png"))
image_4 = canvas.create_image(
    760.0,
    350.0,
    image=image_image_4
)



image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    440.0,
    36.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("Notice Bar.png"))
image_8 = canvas.create_image(
    450.0,
    200.0,
    image=image_image_8
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui2,
    relief="flat"
)
button_1.place(
    x=8.0,
    y=110.0,
    width=211.63711547851562,
    height=35.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=329.0,
    y=111.0,
    width=211.63711547851562,
    height=34.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_url,
    relief="flat"
)
button_3.place(
    x=660.0,
    y=111.0,
    width=211.63711547851562,
    height=34.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("TY 2A.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui4,
    relief="flat"
)
button_4.place(
    x=30,
    y=250,
    width=200,
    height=200
)

button_image_5 = PhotoImage(
    file=relative_to_assets("TY 2B.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui5,
    relief="flat"
)
button_5.place(
    x=250,
    y=250,
    width=190,
    height=200
)

button_image_6 = PhotoImage(
    file=relative_to_assets("TY 3A.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui3,
    relief="flat"
)
button_6.place(
    x=460,
    y=250,
    width=190,
    height=200
)

button_image_7 = PhotoImage(
    file=relative_to_assets("TY 3B.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=open_gui6,
    relief="flat"
)
button_7.place(
    x=680,
    y=250,
    width=190,
    height=200
)



window.resizable(False, False)
window.mainloop()
