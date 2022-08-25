from random import randint
from time import time
from tkinter import *

def make_dot():
    """Creates a dot in a random place in the body canvas"""
    global dot_x, dot_y
    body.delete(ALL)
    dot_x = randint(0, 1500)
    dot_y = randint(0, 600)
    body.create_oval(dot_x, dot_y, dot_x + 100, dot_y + 100, fill = "red")
    body.update()

def dot_click(event):
    """Checks if the user clicked the dot"""
    global dot_x, dot_y, score, click_num
    click_num += 1
    x = event.x
    y = event.y
    if x > dot_x and x < dot_x + 100:
        if y > dot_y and y < dot_y + 100:
            score += 1
            make_dot()

def close_window():
    """Closes the window when called"""
    master.destroy()

"""Creates the test"""
#Sets colours to a variable
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

#Initalises the timer
time_left = StringVar(master=master, value=30)
secs_left = time() + 30
delta_time = secs_left - time()

#Creates the area for the toolbar
toolbar = Frame(master, bg = toolbar_colour, width = 1600, height = 200)
toolbar.place(x = 0, y = 0)

#Creates the timer for the test
test_timer = Label(toolbar, bg = toolbar_colour, fg = text_colour, textvariable = time_left, font = ("TkDefaultFont", 36), image = pixel, width = 160, height = 160, compound = "c")
test_timer.place(x = 20, y = 20)

#Creates the title for the test
test_title = Label(toolbar, bg = toolbar_colour, fg = text_colour, text = "Aim Test", font = ("TkDefaultFont", 36), image = pixel, width = 600, height = 150, compound = "c")
test_title.place(x = 500, y = 20)

#Creates the close button (Needed because of -fullscreen being True)
close_button = Button(toolbar, bg = toolbar_colour, fg = text_colour, text = "Close", font = ("TkDefaultFont", 24), command = close_window, image = pixel, height = 160, width = 160, compound = "c")
close_button.place(x = 1420, y = 20)

#Creates the area for the main content
body = Canvas(master, bg = bg_colour, width = 1600, height = 700)
body.place(x = 0, y = 200)

#Sets loop for the test to run
score = 0
click_num = 0
body.bind("<Button 1>", dot_click)
make_dot()
while delta_time > -1:
    time_left.set(delta_time)
    body.update()
    delta_time = round(secs_left - time())
body.unbind("<Button 1>")
body.delete(ALL)

#Shows the result of the test
score_text = StringVar(body, value = "Score: "+str(score)+"\nAverage Time: "+"{000:3d}".format(round(30000/score))+"ms\nAccuracy: "+"{00:0d}".format(int(round(score/click_num, 2)*100))+"%")
result = Label(body, bg = bg_colour, textvariable = score_text, font = ("TkDefaultFont", 36), image = pixel, width = 1600, height = 600, compound = "c")
result.place(x = 0, y = 0)

master.mainloop()
