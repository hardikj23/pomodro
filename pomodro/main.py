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

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    count_timer(25*60)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_hour = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN*60
    count_timer(work_hour)

    if reps % 8 == 0:
        count_timer(long_break)
        text_label.config(text="Long Break",fg = RED)
    elif reps %2== 0 :
        count_timer(short_break)
        text_label.config(text="Short Break", fg=PINK)
    else:
        count_timer(work_hour)
        text_label.config(text="Work", fg=GREEN)
        tickmark_label = Label(text="✔", fg=GREEN, bg=YELLOW)
        tickmark_label.grid(column=1, row=3)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_timer(count):
    count_min= math.floor(count/60)
    count_sec= count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000,count_timer, count-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=100,bg = YELLOW)


text_label = Label(text="Timer",font=(FONT_NAME,50,"bold"),fg = GREEN,bg = YELLOW)
text_label.grid(column=1,row=0)

start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",highlightthickness=0, command = timer_reset)
reset_button.grid(column=2,row=2)

canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00",font=(FONT_NAME,35,"bold"),fill="white")
canvas.grid(column=1,row=1)




window.mainloop()