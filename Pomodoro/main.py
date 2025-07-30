from tkinter import *
import time

reps = 0
timer_object=None

window = Tk()
window.title("POMODORO")
window.minsize(600,500)
window.config(bg="black", pady=86,padx=85)

def start_timer():
    global reps
    reps += 1
    if reps%2 == 1:
        timer.config(text=f"WORK")
        countdown(25*60)
        window.attributes('-topmost', True)
        window.update()
        window.attributes('-topmost', False)

    elif reps % 8==0:
        timer.config(text=f"LONG BREAK")
        countdown(20*60)
        window.attributes('-topmost', True)
        window.update()
        window.attributes('-topmost', False)
    else:
        timer.config(text=f"BREAK")
        countdown(5*60)
        window.attributes('-topmost', True)
        window.update()
        window.attributes('-topmost', False)

def reset():
    window.after_cancel(timer_object)
    timer.config(text="TIMER")
    time.config(text="00:00")
    global reps
    reps=0

def countdown(number):
    A = number // 60
    B = number % 60
    if A < 10:
        A = "0" + str(A)
    if B < 10:
        B = "0" + str(B)
    time.config(text=f"{A}:{B}")
    if number > 0:
        global timer_object
        timer_object = window.after(1000, countdown, number-1)
    else:
        start_timer()

#window.after(1000,function=,)


timer = Label(text="TIMER", foreground="white", bg="black", font=("Arial",30,"normal"), pady=0, padx=0)
timer.grid(column = 1, row = 0)

time = Label(text="00:00", foreground="white", bg="black", font=("Arial",30,"normal"), pady=60, padx=100)
time.grid(column = 1, row = 1)

start_button = Button(text="START", font=("Arial",20,"normal"), command=start_timer)
start_button.grid(column = 0, row = 2)

reset_button = Button(text="RESET", font=("Arial",20,"normal"), command=reset)
reset_button.grid(column = 2, row = 2)

#countdown(25*60)




window.mainloop()