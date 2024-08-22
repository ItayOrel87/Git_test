import tkinter
from tkinter import ttk

root = tkinter.Tk()
mainframe = ttk.Frame()
mainframe.grid()
root.columnconfigure(0)
root.rowconfigure(0)
hours = tkinter.IntVar()
minutes = tkinter.IntVar()
seconds = tkinter.IntVar()
text = tkinter.StringVar()
sec_time = 0
next_update = ""
field_hour = ttk.Entry(mainframe, textvariable=hours)
field_hour.grid(row=0, column=0)
field_min = ttk.Entry(mainframe, textvariable=minutes)
field_min.grid(row=0, column=1)
field_sec = ttk.Entry(mainframe, textvariable=seconds)
field_sec.grid(row=0, column=2)


def update():
    global sec_time, next_update
    if sec_time == 0:
        text.set("Time's up")
    else:
        sec_time -= 1
        hours_left = sec_time // 3600
        minutes_left = sec_time % 3600 // 60
        second_left = sec_time % 60
        text.set(f"{hours_left}:{minutes_left}:{second_left}")
        next_update = root.after(1000, update)


def start():
    global sec_time, next_update
    if sec_time == 0:
        sec_time = hours.get() * 3600 + minutes.get() * 60 + seconds.get()
        text.set(f"{hours.get()}:{minutes.get()}:{seconds.get()}")
    next_update = root.after(1000, update)


def stop():
    root.after_cancel(next_update)


def reset():
    global sec_time
    hours.set(0)
    minutes.set(0)
    seconds.set(0)
    text.set("0:0:0")
    sec_time = 0


start_button = ttk.Button(mainframe, text="Start", command=start)
start_button.grid(row=1, column=0)
stop_button = ttk.Button(mainframe, text="Stop", command=stop)
stop_button.grid(row=1, column=1)
reset_button = ttk.Button(mainframe, text="Reset", command=reset)
reset_button.grid(row=1, column=2)
timer = ttk.Label(mainframe, textvariable=text)
timer.grid(row=2, column=0, columnspan=3)
root.mainloop()
