from random import randrange
from time import *
from tkinter import *

def clear_body():
    for widget in body.winfo_children():
        widget.destroy()

def guess_confirm():
    global num_guess
    guessed.set(1)
    num_guess = user_guess.get()

def new_num(length):
    correct_num.clear()
    for i in range(length):
        if i == 0:
            correct_num.append(randrange(1,9))
        else:
            correct_num.append(randrange(0,9))            

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
game_title = Label(toolbar, bg = toolbar_colour, fg = text_colour, text = "Memory Test", font = ("TkDefaultFont", 36), image = pixel, width = 600, height = 150, compound = "c")
game_title.place(x = 500, y = 20)

#Creates the close button (Needed because of -fullscreen being True)
close_button = Button(toolbar, bg = toolbar_colour, fg = text_colour, text = "Close", font = ("TkDefaultFont", 24), command = close_window, image = pixel, height = 160, width = 160, compound = "c")
close_button.place(x = 1420, y = 20)

#Creates the area for the main content
body = Frame(master, bg = bg_colour, width = 1600, height = 700)
body.place(x = 0, y = 200)

correct_num = []

loop = True
num_guess = -1
num_length = 1
while loop == True:
    body.update()
    new_num(num_length)
    number = Label(body, bg = bg_colour, width = num_length, height = 1, text = ''.join([str(x) for x in correct_num]), font = ("TkDefaultFont", 24), compound = "c")
    number.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    body.update()
    sleep(num_length)
    number.destroy()
    
    user_guess = Entry(body, bg = bg_colour, width = num_length, font = ("TkDefaultFont", 24))
    user_guess.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    guessed = IntVar()
    confirm_btn = Button(body, bg = bg_colour, width = 7, height = 1, text = "Confirm", font = ("TkDefaultFont", 24), compound = "c", command = guess_confirm)
    confirm_btn.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    
    body.update()
    confirm_btn.wait_variable(guessed)

    clear_body()
    
    if num_guess == ''.join([str(x) for x in correct_num]):
        num_length += 1
    else:
        break
    

score = Label(body, bg = bg_colour, width = 15, height = 2, text = "Your score was\n"+str(num_length - 1), font = ("TkDefaultFont", 24), compound = "c")
score.place(relx = 0.5, rely = 0.5, anchor = CENTER)


master.mainloop()
