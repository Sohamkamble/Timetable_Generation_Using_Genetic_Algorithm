from pathlib import Path
from subprocess import run
import webbrowser
from tkinter import ttk
import sys
from tabulate import tabulate
import pandas as pd
import os
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Button, Canvas ,Label ,PhotoImage, Text, Scrollbar



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame2")



def open_gui3():
    run(["python", str(Path(r".\gui3.py"))])

def open_gui4():
    run(["python", str(Path(r".\Second Year.py"))])

def open_url():
    url = "https://coek.dypgroup.edu.in/academics/syllabus/"  # Replace with your desired URL
    webbrowser.open(url)

def open_excel_sheet(excel_file_path):
    os.startfile(excel_file_path)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def display_excel_on_canvas(canvas, excel_file_path):
    
    # Read the Excel file into a DataFrame
    df = pd.read_excel(excel_file_path)

    # Create a Text widget to display the Excel sheet
    text_widget = Text(canvas, wrap="none", bg="#2C4072",fg="white")
    text_widget.pack(expand=True, fill="both")

    # Create a horizontal scrollbar
    horizontal_scrollbar = Scrollbar(canvas, orient="horizontal", command=text_widget.xview)
    horizontal_scrollbar.pack(side="bottom", fill="x")
    text_widget.configure(xscrollcommand=horizontal_scrollbar.set)

    # Display the DataFrame in the Text widget
    text_widget.insert("end", df.to_string(index=False))

    
window = Tk()

window.geometry("880x600")
window.configure(bg = "#2C4072")


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
    x=660.0,
    y=111.0,
    width=211.63711547851562,
    height=34.0
)

canvas.create_rectangle(
    0.0,
    72.0,
    880.0,
    96.0,
    fill="#FFFFFF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    440.0,
    36.0,
    image=image_image_1
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=print("Button Clicked"),
    relief="flat"
)
button_2.place(
    x=8.0,
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
    command=open_gui3,
    relief="flat"
)
button_3.place(
    x=329.0,
    y=111.0,
    width=211.63711547851562,
    height=34.0
)

zoom_in_button = Button(window, text="3rd Year - A", command=lambda:display_excel_on_canvas(excel_frame,r".\3rd_Year_Division_1.xlsx"), bg="#FF7147", fg="white")
zoom_in_button.place(x=10, y=150)

zoom_in_button1 = Button(window, text="3rd Year - B", command=lambda:display_excel_on_canvas(excel_frame1,r".\3rd_Year_Division_2.xlsx"), bg="#FF7147", fg="white")
zoom_in_button1.place(x=10, y=305)





# Button for zooming in
zoom_in_button = Button(window, text="Final Year", command=print("HE HE"), bg="#FF7147", fg="white")
zoom_in_button.place(x=10, y=530)

# Button for zooming out
zoom_out_button = Button(window, text="Second Year", command=open_gui4, bg="#FF7147", fg="white")
zoom_out_button.place(x=80, y=530)

excel_frame = ttk.Frame(canvas)
excel_frame.place(x=10, y=180, width=860, height=120)

excel_frame1 = ttk.Frame(canvas)
excel_frame1.place(x=10, y=335, width=860, height=120)

window.resizable(False, False)
window.mainloop()
