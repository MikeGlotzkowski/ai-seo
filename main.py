from tkinter import *
from Ai import Ai
import tkinter.font as tkFont

window = Tk()
window.title("SEO AI")
window.geometry('1300x800') # width x length
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=48)
window.option_add("*Font", default_font)

keyword_label = Label(window, text="Key words:")
keyword_label.grid(column=0, row=0)
keyword_input = Entry(window, width=10)
keyword_input.grid(column=1, row=0)


word_count_label = Label(window, text="Word count:")
word_count_label.grid(column=0, row=1)
word_count_input = Entry(window,width=10)
word_count_input.grid(column=1, row=1)

is_list_label = Label(window, text="Include list?")
is_list_label.grid(column=0, row=2)
is_list_input_chk_state = BooleanVar()
is_list_input_chk_state.set(False)
is_list_input = Checkbutton(window, text='', var=is_list_input_chk_state)
is_list_input.grid(column=1, row=2)



response_label = Label(window, text="Result", wraplength=1200, justify="left", font=("Arial", 25))
response_label.grid(columnspan=2, row=5)




def clicked():
    key_words = keyword_input.get()
    word_count = word_count_input.get()
    is_list = is_list_input_chk_state.get() 
    ai = Ai(key_words, int(word_count), is_list) 
    response_label.configure(text = ai.get_text())


action_button = Button(window, text="Go!", command=clicked)
action_button.grid(columnspan=2, row=3)

window.mainloop()