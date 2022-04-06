from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"


def random_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(ger_dict)
    ger_dict.remove(word)
    modified_ger = pandas.DataFrame(ger_dict)
    modified_ger.to_csv('words_to_learn.csv', index=False)
    canvas.itemconfig(language_text, text='German', fill='black')
    canvas.itemconfig(word_text, text=word['word'], fill='black')
    canvas.itemconfig(bg_image, image=card_front)
    flip_timer = window.after(3000, func=flip)


def wrong_ans():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(ger_dict)
    words_to_learn.append(word)
    canvas.itemconfig(language_text, text='German', fill='black')
    canvas.itemconfig(word_text, text=word['word'], fill='black')
    canvas.itemconfig(bg_image, image=card_front)
    flip_timer = window.after(3000, func=flip)


def flip():
    canvas.itemconfig(bg_image, image=card_back)
    canvas.itemconfig(language_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=word['English'], fill='white')


window = Tk()
window.title('Flash Cards')
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip)
try:
    ger_words = pandas.read_csv('words_to_learn.csv')
except FileNotFoundError:
    ger_words = pandas.read_csv('German1000.csv')
ger_dict = ger_words.to_dict(orient='records')
word = {}
words_to_learn = []

card_back = PhotoImage(file='C:/Users/kevs9/PycharmProjects/flashcards/images/card_back.png')
card_front = PhotoImage(file='C:/Users/kevs9/PycharmProjects/flashcards/images/card_front.png')
canvas = Canvas(height=525, width=800)
bg_image = canvas.create_image(400, 262, image=card_front)
language_text = canvas.create_text(400, 150, text='Title', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='Word', font=('Arial', 60, 'bold'))
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

x_image = PhotoImage(file='C:/Users/kevs9/PycharmProjects/flashcards/images/wrong.png')
x = Button(image=x_image, highlightthickness=0, borderwidth=0, command=wrong_ans)
x.grid(column=0, row=1)

correct_image = PhotoImage(file='C:/Users/kevs9/PycharmProjects/flashcards/images/right.png')
correct = Button(image=correct_image, highlightthickness=0, borderwidth=0, command=random_word)
correct.grid(column=1, row=1)

random_word()

window.mainloop()
