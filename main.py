from tkinter import *
import time

DISAPPEARING_TIMER = 10
start_time = None

window = Tk()
window.title("Disappearing text application")
window.minsize(width=700, height=500)

#Label
title_label = Label(window, text="Disappearing text application", fg="white", bg="black")
title_label.pack()

#Entry
entry = Entry()
entry.pack()

#Result
result_label = Label(window, text="Start typing.", fg="white", bg="black")
result_label.pack()


def start_text(event):
    global start_time
    start_time = time.time()



def check_timer():
    global start_time

    if start_time is not None:

        elapsed_time = time.time() - start_time

        if elapsed_time >= DISAPPEARING_TIMER:
            entry.config(state="normal")
            entry.delete(0, END)
            result_label.config(text=f"Start typing to begin the test")

    window.after(100, check_timer)
    window.mainloop()




entry.bind("<Key>", start_text)



window.mainloop()

