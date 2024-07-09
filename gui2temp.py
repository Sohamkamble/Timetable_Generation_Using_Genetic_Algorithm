from pathlib import Path
from subprocess import run
import webbrowser
from tkinter import ttk
import sys
from tabulate import tabulate
import pandas as pd

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Button, Canvas ,Label ,PhotoImage, Text, Scrollbar



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\s2kso\Desktop\Projects\TimeTable Generator\Project Timetable (Latest)\build1\assets\frame2")

def open_gui3():
    run(["python", str(Path(r"C:\Users\s2kso\Desktop\Projects\TimeTable Generator\Project Timetable (Latest)\build1\gui3.py"))])

def open_url():
    url = "https://coek.dypgroup.edu.in/academics/syllabus/"  # Replace with your desired URL
    webbrowser.open(url)




def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



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

zoom_in_button = Button(window, text="3rd Year - Division 1", command=print(""), bg="#FF7147", fg="white")
zoom_in_button.place(x=10, y=150)

def show_excel_file():
    excel_data = pd.read_excel(r"C:\Users\s2kso\Desktop\Projects\TimeTable Generator\Project Timetable (Latest)\build1\3rd_Year_Division_1.xlsx")
    
    # Modify column names
    new_columns = [f"Class {i+1}" for i in range(len(excel_data.columns))]
    excel_data.columns = new_columns

    excel_data_frame = ttk.Treeview(window)
    excel_data_frame["columns"] = excel_data.columns
    excel_data_frame["show"] = "headings"
    
    # Create a style object
    style = ttk.Style()
    
    # Change background color
    style.configure("Treeview", background="white")
    
    # Change foreground color
    style.configure("Treeview.Heading", foreground="white")
    
    for column in excel_data_frame["columns"]:
        excel_data_frame.heading(column, text=column)
        excel_data_frame.column(column, width=160)
    for row in excel_data.itertuples(index=False, name=None):
        excel_data_frame.insert("", "end", values=row)
    excel_data_frame.place(x=10, y=180, height=145, width=860)

    # Adjust horizontal scrollbar's scroll increment
    excel_horizontal_scrollbar = Scrollbar(window, orient="horizontal", command=excel_data_frame.xview)
    excel_horizontal_scrollbar.place(x=10, y=310, width=860)
    excel_data_frame.configure(xscrollcommand=excel_horizontal_scrollbar.set)
    excel_horizontal_scrollbar.config(command=excel_data_frame.xview)
    excel_data_frame.xview_moveto(0)

show_excel_file()




def show_excel_file1():
    excel_data = pd.read_excel(r"C:\Users\s2kso\Desktop\Projects\TimeTable Generator\Project Timetable (Latest)\build1\3rd_Year_Division_2.xlsx")
    
    # Modify column names
    new_columns = [f"Class {i+1}" for i in range(len(excel_data.columns))]
    excel_data.columns = new_columns

    excel_data_frame = ttk.Treeview(window)
    excel_data_frame["columns"] = excel_data.columns
    excel_data_frame["show"] = "headings"
    
    # Create a style object
    style = ttk.Style()
    
    # Change background color
    style.configure("Treeview", background="white")
    
    # Change foreground color
    style.configure("Treeview.Heading", foreground="white")
    
    for column in excel_data_frame["columns"]:
        excel_data_frame.heading(column, text=column)
        excel_data_frame.column(column, width=160)
    for row in excel_data.itertuples(index=False, name=None):
        excel_data_frame.insert("", "end", values=row)
    excel_data_frame.place(x=10, y=362, height=140, width=860)

    # Adjust horizontal scrollbar's scroll increment
    excel_horizontal_scrollbar = Scrollbar(window, orient="horizontal", command=excel_data_frame.xview)
    excel_horizontal_scrollbar.place(x=10, y=500, width=860)
    excel_data_frame.configure(xscrollcommand=excel_horizontal_scrollbar.set)
    excel_horizontal_scrollbar.config(command=excel_data_frame.xview)
    excel_data_frame.xview_moveto(0)



zoom_in_button1 = Button(window, text="3rd Year - Division 2", command=show_excel_file1(), bg="#FF7147", fg="white")
zoom_in_button1.place(x=10, y=331)

# Button for zooming in
zoom_in_button = Button(window, text="Final Year", command=print(""), bg="#FF7147", fg="white")
zoom_in_button.place(x=10, y=530)

# Button for zooming out
zoom_out_button = Button(window, text="Second Year", command=print(""), bg="#FF7147", fg="white")
zoom_out_button.place(x=80, y=530)


window.resizable(True, True)
window.mainloop()
