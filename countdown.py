import tkinter as tk
import time
from plyer import notification

# Window
root = tk.Tk()
root.resizable(False, False)
root.title('Countdown timer')
root.config(bg = 'black')

# Variables
hours = tk.IntVar(value = '00')
secs = tk.IntVar(value = '00')
mins = tk.IntVar(value = '00')

# Labels and entries
tk.Label(text = 'Hours', fg = 'orange', bg= 'black').grid(row = 0, column = 0)
tk.Label(text = 'Mins', fg = 'orange', bg= 'black').grid(row = 0, column = 1)
tk.Label(text = 'Secs', fg = 'orange', bg= 'black').grid(row = 0, column = 2)
tk.Entry(font = 'arial 50', fg = 'white', bg = 'orange', width = 2, textvariable = hours).grid(row = 1, column = 0, padx = 5, pady = 5)
tk.Entry(font = 'arial 50', fg = 'white', bg = 'orange', width = 2, textvariable = mins).grid(row = 1, column = 1, padx = 5, pady = 5)
tk.Entry(font = 'arial 50', fg = 'white', bg = 'orange', width = 2, textvariable = secs).grid(row = 1, column = 2, padx = 5, pady = 5)

# Function
def timer():
    countdown = hours.get() * 3600 + mins.get() * 60 + secs.get()
    
    while countdown > 0:
        min, sec = divmod(countdown, 60)
        hour, min = divmod(min, 60)
        hours.set(f'{hour:02}')
        mins.set(f'{min:02}')
        secs.set(f'{sec:02}')
        countdown -= 1
        root.update()
        time.sleep(1)
    
    notification.notify(
        title = 'It\'s time ',
        message = 'Now! Weak up!',
        app_icon = 'clock.ico',
        timeout = 30
    )

# Button
tk.Button(text = 'Set timer', bg = 'orange', command = timer).grid(row = 2, columnspan = 3, pady = 5)

root.mainloop()