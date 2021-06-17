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
reps =0
first = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global first
    first =0
    reps=0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="Timer")
    check_mark.config(text="")
    
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_mech():
    global reps
    reps+=1
    work_secs = WORK_MIN *60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN *60
    
    if reps % 8 == 0:
        label.config(text ="Break",fg=RED)
        count_down(long_break_secs)
    elif reps%2==0 :
        label.config(text ="Break",fg=PINK)
        count_down(short_break_secs)
    else:
        label.config(text ="Work",fg=GREEN)
        count_down(work_secs)


def start_timer():
    global first  
    
    if first == 0: #if the user presses start again it will have no effect
        first = 1
        timer_mech()
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    mins = math.floor(count/60)
    secs=count%60
    if secs <10:
        
        secs=f"0{secs}"
    if mins <10:
        
        mins=f"0{mins}"
    canvas.itemconfig(timer_text,text=f"{mins}:{secs}")
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        timer_mech()
        marks =""
        work_sess = int(reps/2)
        for _ in range(work_sess):
            marks+="✔"
        check_mark.config(text=marks)
        
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,40,"bold"))
label.grid(column=1,row=0)


canvas = Canvas(width=200,height =224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start = Button(text="Start",highlightthickness=0,command= start_timer)
start.grid(column=0,row=2)

reset = Button(text="Reset",highlightthickness=0,command = reset_timer)
reset.grid(column=2,row=2)

check_mark = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,15))
check_mark.grid(column=1,row=3)





window.mainloop()
