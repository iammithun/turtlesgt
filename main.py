from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
mithun = Tk()
mithun.title("Pomodoro")

# Load image
tomato_img = PhotoImage(file="tomato.png")

# Create canvas and display image
canvas = Canvas(mithun, width=200, height=224)
canvas.create_image(100, 112, image=tomato_img)
canvas.pack()

mithun.mainloop()
