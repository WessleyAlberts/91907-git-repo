from tkinter import *        
from random import randrange, choice

def new_word():
    if score > 5:
        n_or_o = randrange(0, 2)
        if n_or_o == 0:
            current_word.set(choice(words_list))
        else:
            current_word.set(choice(used_words))
    else:
        current_word.set(choice(words_list))
    
def guess_new_word():
    global guess
    guess = "New"
    guessed.set(1)
        
def guess_old_word():
    global guess
    guess = "Old"
    guessed.set(1)
    
def close_window():
    """Closes the window when called"""
    master.destroy()

"""Creates the Main Menu"""
#Sets background colour to a variable
bg_colour = "#858585"
button_colour = "#707070"
toolbar_colour = "#5c5c5c"
text_colour = "#f5f5f5"

#Sets the main menu window
master = Tk()
master.attributes("-fullscreen", True)
master.geometry("1600x900")
master.title("Main Menu")

#Creates an "image" of a pixel
pixel = PhotoImage(width = 1, height = 1)

#Creates the area for the toolbar
toolbar = Frame(master, bg = toolbar_colour, width = 1600, height = 200)
toolbar.place(x = 0, y = 0)

#Creates the title for the game
game_title = Label(toolbar, bg = toolbar_colour, fg = text_colour, text = "Vocabulary Memory Test", font = ("TkDefaultFont", 36), image = pixel, width = 600, height = 150, compound = "c")
game_title.place(x = 500, y = 20)

#Creates the close button (Needed because of -fullscreen being True)
close_button = Button(toolbar, bg = toolbar_colour, fg = text_colour, text = "Close", font = ("TkDefaultFont", 24), command = close_window, image = pixel, height = 160, width = 160, compound = "c")
close_button.place(x = 1420, y = 20)

#Creates the area for the main content
body = Frame(master, bg = bg_colour, width = 1600, height = 700)
body.place(x = 0, y = 200)

with open("C:\\Users\\wesel\\Desktop\\Cos\\2022\\91907_wessley_alberts\\91907 git repo\\code\\words_alpha.txt") as words_file:
    words_list = []
    for line in words_file:
        words_list.append(line)

guess = ""
used_words = []
current_word = StringVar(body)
score = 0
loop = True
while loop == True:
    body.update()
    new_word()
    word = Label(body, bg = bg_colour, width = 31, height = 2, textvariable = current_word, font = ("TkDefaultFont", 24), compound = "c")
    word.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    body.update()
    guessed = IntVar()
    new_btn = Button(body, bg = bg_colour, width = 8, height = 1, text = "New word", font = ("TkDefaultFont", 24), compound = "c", command = guess_new_word)
    new_btn.place(relx = 0.4, rely = 0.6, anchor = CENTER)
    old_btn = Button(body, bg = bg_colour, width = 8, height = 1, text = "Old word", font = ("TkDefaultFont", 24), compound = "c", command = guess_old_word)
    old_btn.place(relx = 0.6, rely = 0.6, anchor = CENTER)
    body.update()
    body.wait_variable(guessed)
    
    print(used_words)
    print(current_word.get())
    if guess == "New":
        if current_word.get() in used_words:
            break
        else:
            score += 1
    elif guess == "Old":
        if current_word.get() in used_words:
            score += 1
        else:
            break
    print(score)
    used_words.append(current_word.get())

score_string = StringVar(body, "Your score was\n" + str(score))
score = Label(body, bg = bg_colour, width = 15, height = 2, textvariable = score_string, font = ("TkDefaultFont", 24), compound = "c")
score.place(relx = 0.5, rely = 0.5, anchor = CENTER)

master.mainloop()
