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
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\s2kso\Desktop\Projects\TimeTable Generator\Project Timetable(Temp not for running\build1\assets\frame3")

def open_gui2():
    run(["python", str(Path(r"C:\Users\s2kso\Desktop\Projects\TimeTable Generator\Project Timetable(Temp not for running\build1\gui2.py"))])

def open_url():
    url = "https://coek.dypgroup.edu.in/academics/syllabus/"  # Replace with your desired URL
    webbrowser.open(url)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("880x550")
window.configure(bg = "#2C4072")
window.title("Second Year : Division A")
week = ["Mon","Tue","Wed","Thu","Fri"]

timetable1 = pd.read_excel(r"C:\Users\s2kso\Desktop\Projects\TimeTable Generator\Project Timetable(Temp not for running\build1\2nd_Year_Division_1.xlsx")
timetable1
replacement_dict = {
    "LA-Mrs. Chava": 1,
    "FN-Mr. S Patil": 1,
    "DS-Mr. G V Patil": 1,
    "PP-Mr. Metkari": 1,
    "DMS-Ms. A Patil": 1,
    "LA-Mrs. Chavan":1,
    "No class": 0
}

# Replace the values in the timetable DataFrame using the dictionary
timetable = timetable1.replace(replacement_dict)

# Print the updated timetable
print(timetable)

timetable = timetable.drop("Unnamed: 0", axis=1)
timetable
timetable.columns = ['class 1', 'class 2', 'class 3', 'class 4', 'class 5', 'class 6']
timetable


# Print the updated timetable
print(timetable)

total_classes_per_day = timetable.iloc[:, :].sum(axis=1).tolist()
# Calculate the total number of classes for each day


# Now total_classes_per_day contains the total classes per day as a list
print(total_classes_per_day)

total_hours = sum(total_classes_per_day)
print(total_hours)



colors = ["#A2B7FF","#2C4072","#FF7147","#E2A08C",'#C6C6C6']

replacement_dict1 = {
    "LA-Mrs. Chavan": "LA",
    "FN-Mr. S Patil": "FA",
    "DS-Mr. G V Patil": "DS",
    "PP-Mr. Metkari": "PP",
    "DMS-Ms. A Patil": "DMS",
    "No class": " "
}

# Replace the values in the timetable DataFrame using the dictionary
timetable2 = timetable1.replace(replacement_dict1)

# Print the updated timetable
print(timetable2)

teacher_count = {}

# Loop through each row in the timetable
for row in timetable2.itertuples():
    # Loop through each cell in the row
    for cell in row:
        # Check if the cell contains a teacher name
        if cell in ["LA", "FA", "DS", "PP", "DMS"]:
            # If the teacher name is not already in the dictionary, add it with a count of 0
            if cell not in teacher_count:
                teacher_count[cell] = 0
            # Increment the count of the teacher name
            teacher_count[cell] += 1

# Print the count of each teacher
for teacher, count in teacher_count.items():
    print(f"{teacher}: {count}")

teachers, counts = zip(*teacher_count.items())

print(teacher_count)

total_count = sum(teacher_count.values())

# Calculate the average count
average_count = total_count / len(teacher_count)

# Display the average count
print(f"Average count of teachers: {average_count}")







# Get the total number of zeros for each day
total_zeros_per_day = (timetable == 0).sum(axis=1)

free_slots = sum(total_zeros_per_day)
print(free_slots)





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
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    146.0,
    225.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    146.0,
    402.0,
    image=image_image_2
)


image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    439.0,
    225.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    439.0,
    402.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    734.0,
    225.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    734.0,
    402.0,
    image=image_image_6
)

canvas.create_text(
    19.0,
    199.0,
    anchor="nw",
    text="TOTAL HOURS",
    fill="#000000",
    font=("JuliusSansOne Regular", 11 * -1)
)

canvas.create_text(
    115.0,
    208.0,
    anchor="nw",
    text=total_hours,
    fill="#000000",
    font=("Armata Regular", 36 * -1)
)

canvas.create_text(
    410.0,
    208.0,
    anchor="nw",
    text=average_count,
    fill="#000000",
    font=("Armata Regular", 36 * -1)
)

canvas.create_text(
    712.0,
    212.0,
    anchor="nw",
    text=free_slots,
    fill="#000000",
    font=("Armata Regular", 36 * -1)
)

canvas.create_text(
    300.0,
    199.0,
    anchor="nw",
    text="SUBJECT HOURS",
    fill="#000000",
    font=("JuliusSansOne Regular", 11 * -1)
)

canvas.create_text(
    611.0,
    199.0,
    anchor="nw",
    text="FREE SLOTS ",
    fill="#000000",
    font=("JuliusSansOne Regular", 11 * -1)
)

canvas.create_rectangle(
    0.0,
    72.0,
    880.0,
    96.0,
    fill="#FFFFFF",
    outline="")

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    440.0,
    36.0,
    image=image_image_7
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



# Generate the x-axis values (day numbers)

fig_1 = Figure(figsize=(2.5, 2.5), facecolor="#A2B7FF")
ax_1 = fig_1.add_subplot()
ax_1.set_facecolor("#A2B7FF")
ax_1.fill_between(x=week, y1=total_classes_per_day, alpha=0.7, color = "#FF7147")
ax_1.tick_params(labelsize=6, colors="Black")
ax_1.plot(week, total_classes_per_day, color="#2C4072")
ax_1.grid(visible=True)
fig_1.suptitle("HOURS IN WEEK")

canvas = FigureCanvasTkAgg(figure=fig_1, master=window)
canvas.draw()
canvas.get_tk_widget().place(x=20, y=280)




fig_2 = Figure(figsize=(2.5, 2.5), facecolor="#FFFFFF")
ax_2 = fig_2.add_subplot()  # 2 rows, 1 column, subplot 2
ax_2.pie(counts, labels=teachers, autopct='%1.0f%%', startangle=310, colors= colors)
ax_2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
ax_2.set_title("SUBJECT HOURS")

canvas = FigureCanvasTkAgg(figure=fig_2, master=window)
canvas.draw()
canvas.get_tk_widget().place(x=315, y=279)





#Bar chart


# Generate the x-axis values (day numbers)


fig_3 = Figure(figsize=(2.5, 2.5), facecolor="#E2A08C")
ax_3 = fig_3.add_subplot()
ax_3.set_facecolor("#E2A08C")
ax_3.tick_params(labelsize=6, colors="Black")
ax_3.bar(week, total_zeros_per_day, color="#2C4072")
ax_3.set_ylim(0, 4)
fig_3.suptitle("FREE SLOTS")

canvas = FigureCanvasTkAgg(figure=fig_3, master=window)
canvas.draw()
canvas.get_tk_widget().place(x=608, y=280)


window.resizable(False, False)
window.mainloop()
