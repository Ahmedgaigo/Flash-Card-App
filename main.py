from tkinter import *
import pandas
from random import choice as c

BACKGROUND_COLOR = "#B1DDC6"
random_card = {}
words_list = {}

# ------------------------ data stuff ------------------------ #
try:
	data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
	original_data = pandas.read_csv("data/french_words.csv")
	words_list = original_data.to_dict(orient="records")
else:
	words_list = data.to_dict(orient='records')


def next_word():
	global random_card, flip_timer
	window.after_cancel(flip_timer)
	random_card = c(words_list)
	canvas.itemconfig(photo, image=front_image)
	canvas.itemconfig(language, text="French", fill="black")
	canvas.itemconfig(word, text=random_card["French"], fill="black")
	flip_timer = window.after(3000, func=flip_card)


# ------------------------ save progress ------------------------ #
def is_known():
	words_list.remove(random_card)
	# converting it to a csv file
	pandas.DataFrame(words_list).to_csv("data/words_to_learn.csv", index=False)
	next_word()


def flip_card():
	canvas.itemconfig(photo, image=back_image)
	canvas.itemconfig(language, text="English", fill="white")
	canvas.itemconfig(word, text=random_card["English"], fill="white")
# ------------------------------------------------------------ #


# creating the window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# importing images to use
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# creating a canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# to add image, we use canvas
photo = canvas.create_image(400, 263, image=front_image)
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_word, bg=BACKGROUND_COLOR)
unknown_button.grid(column=0, row=1)

right_button = Button(image=right_image, highlightthickness=0, command=is_known, bg=BACKGROUND_COLOR)
right_button.grid(column=1, row=1)

next_word()

window.mainloop()
