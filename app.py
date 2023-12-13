from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 40, "bold")
FR_LANG = "French"
EN_LANG = "English"
french_word = "Bonjour"
english_word = ""

def flip_card():
    pass




# ----------------------------- UI Setup ---------------------------------------- #
window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR, width=700, height=500)
window.title("Flashy Cards")

card_photo = PhotoImage(file="images/card_back.png")
card_button = Label(image=card_photo, background=BACKGROUND_COLOR)
card_button.grid(row=1, column=1, columnspan=3)

wrong_photo = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_photo, borderwidth=0, highlightthickness=0)
wrong_button.grid(row=2, column=1)

right_photo = PhotoImage(file="images/right.png")
right_button = Button(image=right_photo, borderwidth=0, highlightthickness=0)
right_button.grid(row=2, column=3)

flip_button = Button(height=3, width=6,text="Flip", borderwidth=0, highlightthickness=0, font=("Comic Sans", 24))
flip_button.grid(row=2, column=2)
flip_button.config(command=flip_card)

language_label = Label(text=FR_LANG, font=LANG_FONT, background=BACKGROUND_COLOR, fg="black")
language_label.grid(row=0, column=2)
word_label = Label(text=french_word, font=WORD_FONT, fg="white")
word_label.grid(row=1, column=2)


window.mainloop()