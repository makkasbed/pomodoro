import math
from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_second = WORK_MIN * 60
    short_break_second = SHORT_BREAK_MIN * 60
    long_break_second = LONG_BREAK_MIN * 60

    count_down(work_second)

    if reps % 8 == 0:
        count_down(long_break_second)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 ==0:
        count_down(short_break_second)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_second)
        timer_label.config(text="Work", fg=GREEN)


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_button.config(text="")
    global reps
    reps = 0




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minute = math.floor(count / 60)
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
        check_button.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer, bg=YELLOW, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, bg=YELLOW, background=YELLOW, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_button = Label(fg=GREEN, bg=YELLOW)
check_button.grid(column=1, row=3)

window.mainloop()
