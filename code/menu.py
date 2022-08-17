from tkinter import *

def close_window():
    master.destroy()

def test():
    return "test"
        
"""Creates the layout of the Main Menu"""
#Sets background colour to a variable
bg_colour = "#a8a8a8"
toolbar_colour = "#111fff"

#Sets the main menu window
master = Tk()
master.configure(bg = (bg_colour))
master.attributes("-fullscreen", True)
master.geometry("1600x900")
master.title("Main Menu")

#Creates an "image" of a pixel
pixel = PhotoImage(width = 1, height = 1)


toolbar = Frame(master, bg = toolbar_colour, width = 1600, height = 100)
toolbar.place(x = 0, y = 0)

game_title = Label(toolbar, bg = toolbar_colour, text = "17 character name", font = ("TkDefaultFont", 36), image = pixel, width = 400, height = 50, compound = "c")
game_title.place(x = 600, y = 10)

close_button = Button(toolbar, bg = toolbar_colour, text = "Close", font = ("TkDefaultFont", 24), command = close_window, image = pixel, height = 50, width = 50, compound = "c")
close_button.place(x = 1500, y = 10)

body = Frame(master, bg = bg_colour, width = 1600, height = 800)
body.place(x = 0, y = 100)

test_button1 = Button(body, bg = bg_colour, text = "Test", font = ("TkDefaultFont", 36), command = "Test", image = pixel, height = 150, width = 150, compound = "c")
test_button1.place(x = 100, y = 50)
test_button2 = Button(body, bg = bg_colour, text = "Test", font = ("TkDefaultFont", 36), command = "Test", image = pixel, height = 150, width = 150, compound = "c")
test_button2.place(x = 100, y = 500)
test_button3 = Button(body, bg = bg_colour, text = "Test", font = ("TkDefaultFont", 36), command = "Test", image = pixel, height = 150, width = 150, compound = "c")
test_button3.place(x = 1000, y = 50)
test_button4 = Button(body, bg = bg_colour, text = "Test", font = ("TkDefaultFont", 36), command = "Test", image = pixel, height = 150, width = 150, compound = "c")
test_button4.place(x = 1000, y = 500)

master.mainloop()
