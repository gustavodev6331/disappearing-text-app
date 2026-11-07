from tkinter import *
import time

DISAPPEARING_TIMER = 10
start_time = None

window = Tk()
window.title("Disappearing text application")
window.minsize(width=700, height=500)
window.config(bg="#202124")


main_frame = Frame(window, bg="#202124")
main_frame.pack(fill="both", expand=True, padx=30, pady=25)

#Label
title_label = Label(main_frame, text="Dangerous text application", fg="white", bg="black")
title_label.pack()

#count_down
count_label = Label(main_frame, text="10 seconds", fg="red", bg="black")
count_label.pack()

#Entry
text = Text(main_frame)
text.pack()

#Result
result_label = Label(main_frame, text="Keep writing. Don't stop for over than 10 seconds!", fg="white", bg="black")
result_label.pack()


def start_text(event):
    global start_time
    start_time = time.time()



def check_timer():
    global start_time

    if start_time is not None:

        elapsed_time = time.time() - start_time
        remaining_time = max(0, int(DISAPPEARING_TIMER - elapsed_time))
        count_label.config(text=f"{int(remaining_time + 1)} seconds")
        result_label.config(text=f"Keep writing. Don't stop for over than 10 seconds!")

        if elapsed_time >= DISAPPEARING_TIMER:
            text.config(state="normal")
            text.delete("1.0", END)
            result_label.config(text=f"Start typing to re-start the test")
            start_time = None
            count_label.config(text="Time over")


    window.after(100, check_timer)





text.bind("<Key>", start_text)


window.after(100, check_timer)
window.mainloop()

