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
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    stop = window.after_cancel(timer)
    #timer 00:00
    #timer label
    #check marks to none
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    label_check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Break", fg=PINK)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Long Break", fg=RED)
    else:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    if count_min == 0:
        count_min = "00"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✓"
        label_check.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

#Label
label_timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
label_timer.grid(row=0, column=2)

label_check = Label(bg=YELLOW)
label_check.grid(row=4, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 117, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=2, column=2)



#buttons
button_start = Button(text="Start", command=start_timer)
button_reset = Button(text="Reset", command=reset_timer)
button_start.grid(row=3, column=1)
button_reset.grid(row=3, column=3)

window.mainloop()