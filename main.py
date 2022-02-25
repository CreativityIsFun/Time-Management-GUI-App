from tkinter import *
import math

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
timer_running = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer_running
    window.after_cancel(timer_running)
    canvas.itemconfig(timer_text, text = "00:00")
    timer_label.config(text = "Timer")
    pomodoro_count.config(text = "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    #If it's the 8th time:
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text = "Take a long break!", fg = RED)
    # If it's the 2nd/4th/6th time:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text = "Take a short break!", fg = PINK)
    # If it's the 1st/3rd/5th/7th time:
    else:
        count_down(work_sec)
        timer_label.config(text = "Do your work now!", fg = GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global timer_running
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        timer_running = window.after(1000, count_down, count-1)
    elif count == 0:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        pomodoro_count.config(text = marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady = 50, bg = YELLOW)


timer_label = Label(text = "Timer", font=(FONT_NAME, 25, "bold"), bg = YELLOW, fg = GREEN)
timer_label.grid(column = 1, row = 0)
#timer_label.pack()

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_image)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "black", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)
#canvas.pack()


start_button = Button(text = "Start", command = start_timer, highlightthickness=0)
start_button.grid(column = 0, row = 2)
#start_button.pack()

pomodoro_count = Label(font = (FONT_NAME, 12, "bold"), bg = YELLOW, fg = GREEN)
pomodoro_count.grid(column = 1, row = 3)
#pomodoro_count.pack()



reset_button = Button(text = "Reset", command = reset_timer, highlightthickness=0)
reset_button.grid(column = 2, row = 2)
#reset_button.pack()


window.mainloop()