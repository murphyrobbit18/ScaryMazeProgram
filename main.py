from guizero import App, PushButton, Text, Window, Picture

def changeCursor(widget, cursor_style):
    widget.tk.config(cursor = cursor_style)
   
def open_window():
    selectionScreen.show()
    selectionScreen.full_screen = True

def open_lvlOne():
    lvlOne.show()
    lvlOne.full_screen = True
 
def open_lvlTwo():
    lvlTwo.show()
    lvlTwo.full_screen = True

def open_lvlThree():
    lvlThree.show()
    lvlThree.full_screen = True

app = App(title="Scary Maze", bg='#15ffff')
app.full_screen = True
changeCursor(app, "pirate")

title = Text(app, text="\nThe Maze", font="Courier Bold", size= 30)
description = Text(app, text="\nTest your skills!", font="Courier")
info = Text(app, text= "Try to reach the goal without touching the walls\nHow steady is your hand?\nLet's find out! Try and beat all four level!", font="Courier")
noisePrompt = Text(app, text="\nsound effects will help\n", font="Courier")

playButton = PushButton(app, text="Play", command = open_window)
playButton.text_color = "#ffffff"
playButton.bg = "#000000"

selectionScreen = Window(app, title = "Control Selection" , bg = "#15ffff")
controlChoices = Text(selectionScreen, text= "\n\nSelect a control method from the choices below:\n", font = "Courier", size= 18)
changeCursor(selectionScreen, "pirate")

mouse = PushButton(selectionScreen, text = "Mouse", command= open_lvlOne)
mouse.text_color = "#ffffff"
mouse.bg = "#000000"

lvlOne = Window(app, title = "Level One", bg='#000000')
space = Text(lvlOne, text = "\n\n\n")
background1 = Picture(lvlOne, image = "levelOne.png", width=800, height = 800)
changeCursor(lvlOne, "pirate")

lvlProgress = PushButton(lvlOne, command = open_lvlTwo, width =7, height = 1)
lvlProgress.bg = "#ff4405"
lvlProgress.text_color = "#ff4405"

lvlTwo = Window(app, title = "Level Two", bg='#000000')
space2 = Text(lvlOne, text = "\n\n\n")
background2 = Picture(lvlTwo, image = "levelTwo.png", width=800, height = 800)
changeCursor(lvlTwo, "pirate")


lvlProgress2 = PushButton(lvlTwo, command = open_lvlThree, width =5, height = 1)
lvlProgress2.bg = "#ff4405"
lvlProgress2.text_color = "#ff4405"

lvlThree = Window(app, title = "Level Three", bg='#000000')
space3 = Text(lvlOne, text = "\n\n\n")
background3 = Picture(lvlThree, image = "levelThree.png", width=800, height = 800)
changeCursor(lvlThree, "pirate")

selectionScreen.hide()
lvlOne.hide()
lvlTwo.hide()
lvlThree.hide()

app.display()