#! python3
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
LONG_BREAK_MIN = 30
marks = ''

# ---------------------------- CLASS ------------------------------------- #


class Pomodoro:
    def __init__(self, root):
        self.marks = ''
        self.reps = 0
        self.root = root
        root.title('Pomodoro')
        root.config(padx=100, pady=50, bg=YELLOW)

        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.photo = PhotoImage(file='C:/Users/kevs9/PycharmProjects/pomodoro/tomato.png')
        self.canvas.create_image(100, 112, image=self.photo)
        self.timer_text = self.canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
        self.canvas.grid(column=1, row=1)

        self.title = Label(text='Timer', font=(FONT_NAME, 25, 'bold'), fg=GREEN, bg=YELLOW)
        self.title.grid(column=1, row=0)

        self.check = Label(fg=GREEN, font=(FONT_NAME, 15), bg=YELLOW)
        self.check.grid(column=1, row=3)

        self.start_button = Button(text='Start', command=self.start_timer)
        self.start_button.grid(column=0, row=2)

        self.reset_button = Button(text='Reset', command=self.reset_timer)
        self.reset_button.grid(column=2, row=2)

    def reset_timer(self):
        self.root.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_text, text='00:00')
        self.title.config(text='Timer', fg=GREEN)
        self.check.config(text='')

    def start_timer(self):
        self.reps += 1
        if self.reps % 8 == 0:
            self.title.config(text='Break', fg=PINK)
            self.count_down(LONG_BREAK_MIN * 60)
        elif self.reps % 2 == 0:
            self.title.config(text='Break', fg=PINK)
            self.count_down(SHORT_BREAK_MIN * 60)
        else:
            self.title.config(text='Work', fg=GREEN)
            self.count_down(WORK_MIN * 60)

    def count_down(self, count):
        min = count // 60
        sec = count % 60
        self.canvas.itemconfig(self.timer_text, text=f'{min}:{sec:02}')
        if count > 0:
            self.timer = self.root.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()
            self.marks = ''
            for i in range(int(self.reps / 2)):
                if len(self.marks) == 4:
                    self.marks = ''
                self.marks += '✔'
            self.check.config(text=self.marks)


# ---------------------------- TIMER RESET ------------------------------- #
# def reset_timer():
#     window.after_cancel(timer)
#     canvas.itemconfig(timer_text, text='00:00')
#     title.config(text='Timer', fg=GREEN)
#     check.config(text='')
#     global reps, marks
#     reps = 0
#     marks = ''
#
#
# # ---------------------------- TIMER MECHANISM ------------------------------- #
# def start_timer():
#     global reps
#     reps += 1
#     if reps % 8 == 0:
#         title.config(text='Break', fg=PINK)
#         count_down(LONG_BREAK_MIN * 60)
#     elif reps % 2 == 0:
#         title.config(text='Break', fg=PINK)
#         count_down(SHORT_BREAK_MIN * 60)
#     else:
#         title.config(text='Work', fg=GREEN)
#         count_down(WORK_MIN * 60)
#
#
# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# def count_down(count):
#     global marks
#     min = count // 60
#     sec = count % 60
#     canvas.itemconfig(timer_text, text=f'{min}:{sec:02}')
#     if count > 0:
#         global timer
#         timer = window.after(1000, count_down, count - 1)
#     else:
#         start_timer()
#         marks = ''
#         for i in range(int(reps / 2)):
#             if len(marks) == 4:
#                 marks = ''
#             marks += '✔'
#         check.config(text=marks)
#
#
# # ---------------------------- UI SETUP ------------------------------- #
# window = Tk()
# window.title('Pomodoro')
# window.config(padx=100, pady=50, bg=YELLOW)
#
# canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# photo = PhotoImage(file='C:/Users/kevs9/PycharmProjects/pomodoro/tomato.png')
# canvas.create_image(100, 112, image=photo)
# timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
# canvas.grid(column=1, row=1)
#
# title = Label(text='Timer', font=(FONT_NAME, 25, 'bold'), fg=GREEN, bg=YELLOW)
# title.grid(column=1, row=0)
#
# check = Label(fg=GREEN, font=(FONT_NAME, 15), bg=YELLOW)
# check.grid(column=1, row=3)
#
# start_button = Button(text='Start', command=start_timer)
# start_button.grid(column=0, row=2)
#
# reset_button = Button(text='Reset', command=reset_timer)
# reset_button.grid(column=2, row=2)
#
# window.mainloop()

root = Tk()
pomodoro = Pomodoro(root)
root.mainloop()
