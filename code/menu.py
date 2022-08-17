from tkinter import *

def close_window():
    master.destroy()

def test():
    return "test"
        
"""Creates the layout of the Main Menu"""
#Sets background colour to a variable
bg_colour = "#858585"
button_colour = "#707070"
toolbar_colour = "#5c5c5c"
text_colour = "#f5f5f5"

#Sets the main menu window
master = Tk()
master.configure(bg = (bg_colour))
master.attributes("-fullscreen", True)
master.geometry("1600x900")
master.title("Main Menu")

#Creates an "image" of a pixel
pixel = PhotoImage(width = 1, height = 1)


toolbar = Frame(master, bg = toolbar_colour, width = 1600, height = 200)
toolbar.place(x = 0, y = 0)

game_title = Label(toolbar, bg = toolbar_colour, fg = text_colour, text = "17 character name", font = ("TkDefaultFont", 36), image = pixel, width = 600, height = 150, compound = "c")
game_title.place(x = 500, y = 20)

close_button = Button(toolbar, bg = toolbar_colour, fg = text_colour, text = "Close", font = ("TkDefaultFont", 24), command = close_window, image = pixel, height = 160, width = 160, compound = "c")
close_button.place(x = 1420, y = 20)

body = Frame(master, bg = bg_colour, width = 1600, height = 700)
body.place(x = 0, y = 200)

test_button1 = Button(body, bg = button_colour, text = "Test", font = ("TkDefaultFont", 36), command = "test", image = pixel, height = 220, width = 550, compound = "c")
test_button1.place(x = 200, y = 100)
test_button2 = Button(body, bg = button_colour, text = "Test", font = ("TkDefaultFont", 36), command = "test", image = pixel, height = 220, width = 550, compound = "c")
test_button2.place(x = 200, y = 380)
test_button3 = Button(body, bg = button_colour, text = "Test", font = ("TkDefaultFont", 36), command = "test", image = pixel, height = 220, width = 550, compound = "c")
test_button3.place(x = 850, y = 100)
test_button4 = Button(body, bg = button_colour, text = "Test", font = ("TkDefaultFont", 36), command = "test", image = pixel, height = 220, width = 550, compound = "c")
test_button4.place(x = 850, y = 380)

master.mainloop()
