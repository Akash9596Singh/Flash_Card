
BACKGROUND_COLOR = "#B1DDC6"
import pandas as pd
from tkinter import *
import random
current_card={}
data_record={}
try:
    data_set=pd.read_csv('/Users/akashsingh/Desktop/100Days Python/Day31/flash-card-project-start/data/words_to_learn.csv')

except FileNotFoundError:
    original_record = pd.read_csv('/Users/akashsingh/Desktop/100Days Python/Day31/flash-card-project-start/data/french_words.csv')
    data_record = original_record.to_dict(orient="records")
else:
    data_record = data_set.to_dict(orient="records")
# print(data_record)

def is_known():
    window.after_cancel(flip_timer)
    data_record.remove(current_card)
    # print(len(data_record))
    data=pd.DataFrame(data_record)
    data.to_csv("/Users/akashsingh/Desktop/100Days Python/Day31/flash-card-project-start/data/words_to_learn.csv",index=False)


    next_card()


def generate_english():

    english_word = current_card['English']
    canvas.itemconfig(card, image=card_back_image)
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=english_word)
    # canvas.create_text(400,450,text="Did you know the answer?", fill='black', font=('ariel', 40))
    canvas.itemconfig(question,text="Did you know the answer?")




def next_card():
    global current_card,flip_timer
    current_card=random.choice(data_record)
    french_word=current_card['French']
    # print(french_word)
    # print(english_word)
    canvas.itemconfig(card,image=card_front_image)
    canvas.itemconfig(title,text="French")
    canvas.itemconfig(word,text=french_word)
    canvas.itemconfig(question,text="Do you know the answer")
    flip_timer=window.after(3000,func=generate_english)



window=Tk()

window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)
window.title('Flashy')
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_image=PhotoImage(file='/Users/akashsingh/Desktop/100Days Python/Day31/flash-card-project-start/images/card_front.png')
card_back_image=PhotoImage(file='/Users/akashsingh/Desktop/100Days Python/Day31/flash-card-project-start/images/card_back.png')
card=canvas.create_image(400,263,image=card_front_image)
question=canvas.create_text(400, 450, text="", fill='black', font=('ariel', 40))


title=canvas.create_text(400, 150, text="", fill='black', font=('ariel', 40))
word=canvas.create_text(400, 263, text="", fill='black', font=('ariel', 40,'bold'))
canvas.grid(row=0,column=0,columnspan=2)


#BUTTON
check_image=PhotoImage(file="/Users/akashsingh/Desktop/100Days Python/Day31/flash-card-project-start/images/right.png")
# tick_button=Button(image=check_image,highlightthickness=0,padx=50,bg=BACKGROUND_COLOR)
# tick_button.grid(row=1,column=1)
#
#
cross_image=PhotoImage(file="/Users/akashsingh/Desktop/100Days Python/Day31/flash-card-project-start/images/wrong.png")
# cross_button=Button(image=cross_image,highlightthickness=0,padx=50,background=BACKGROUND_COLOR)
# cross_button.grid(row=1,column=0)


tick_button = Button(image=check_image, highlightthickness=0, padx=50, bg=BACKGROUND_COLOR,
                         command=is_known)
tick_button.grid(row=1, column=1)



cross_button = Button(image=cross_image, highlightthickness=0, padx=50, background=BACKGROUND_COLOR,
                      command=next_card)
cross_button.grid(row=1, column=0)

next_card()



window.mainloop()

