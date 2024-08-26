import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN, MOUSEMOTION
import explorerhat as eh


pygame.init()

res = (720,720)
screen = pygame.display.set_mode(res)
menuBackground = pygame.display.set_mode((625,600))

titleFont = pygame.font.SysFont("Courier", 30, bold = True)

cursor_size = 7
red = (255,0,0)
aqua = (1, 255, 255)

def drawTitle(text, font, text_col, x, y):
    title = font.render(text, True, text_col)
    menuBackground.blit(title, (x,y))

descriptionFont = pygame.font.SysFont("Courier", 20)

def drawText(text, font, text_col, x, y):
    description = font.render(text, True, text_col)
    menuBackground.blit(description, (x,y))

captionFont = pygame.font.SysFont("Courier", 15, italic = True)

def captionText(text, font, text_col, x, y):
    caption = font.render(text, True, text_col)
    menuBackground.blit(caption, (x,y))

def menu():

    menuBackground.fill(aqua)

    drawTitle("The Maze", titleFont, (0, 0, 0), 260, 15)
   
    drawText("Test your skills!", descriptionFont, (0,0,0), 225, 100)
    drawText("Try to reach the goal without touching the walls.", descriptionFont, (0,0,0), 25, 150)
    drawText("How steady is your hand?", descriptionFont, (0,0,0), 195, 200)
    drawText("Lets find out! Try to beat all three levels", descriptionFont, (0,0,0), 65, 250)
   
    captionText("sound effects will help", captionFont, (0, 0, 0), 225, 300)
   
    menuButton = pygame.Surface((100, 40))
    menuButton.fill((0, 0, 0))
    buttonfont = pygame.font.SysFont("Courier", 25, bold = True)
    text = buttonfont.render(" Play", True, (255, 255, 255))
   
    menuButton.blit(text, (5, 5))
    menuBackground.blit(menuButton, (265, 350))


def lvlOne():
   
    #aqua = (1, 255, 255)
    #red = (255,0,0)
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(220,45,260,50))
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(220,90,150,400))
    pygame.draw.rect(menuBackground, red, pygame.Rect(450,45,80,50))

   
    #mouse = pygame.mouse.get_pos()
    #print(mouse)

def lvlTwo():
   
    aqua = (1, 255, 255)
    red = (255,0,0)

    pygame.draw.rect(menuBackground, aqua, pygame.Rect(150,45,370,50))
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,45,50,90))
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,135,430,50))
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(480,165,50,90))
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,225,430,50))
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,235,50,90))
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,315,430,50))
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(460,315,70,110))
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,395,430,40))
    pygame.draw.rect(menuBackground, red, pygame.Rect(100,395,80,40))

    mouse = pygame.mouse.get_pos()
    print(mouse)

def lvlThree():
   
    aqua = (1, 255, 255)
    red = (255,0,0)

    pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,395,430,40))
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(490,355,40,60))
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,335,430,40))
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,275,40,60))
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,235,140,50))
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,235,300,20))
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(400,195, 20, 60))
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(280,195,120,20))
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(315,80,20,65))
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(260,145,20,70))
    pygame.draw.rect(menuBackground, aqua, pygame.Rect(260,145,75,20))
    pygame.draw.rect(menuBackground, red, pygame.Rect(300,35,50,70))

def endScreen():
   
    goat = pygame.image.load("goat.png")
    menuBackground.blit(goat, (0, 0))
    drawTitle("Thank you for playing!", titleFont, (0, 0, 0), 160, 15)

    menuButton = pygame.Surface((190, 40))
    menuButton.fill((0, 0, 0))
    buttonfont = pygame.font.SysFont("Courier", 25, bold = True)
    text = buttonfont.render(" Play Again", True, (255, 255, 255))

    menuButton.blit(text, (5, 5))
    menuBackground.blit(menuButton, (220, 525))

def jumpScare():

    goat = pygame.image.load("goat.png")
    menuBackground.blit(goat, (0, 0))

class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("cursor_image.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

cursor = Cursor()

pygame.mouse.set_visible(False)

goatScream = pygame.mixer.Sound('goatScream.wav')

currentlvl= "menu"

menu()

while True:

    if currentlvl == "menu":
        menu()

    elif currentlvl == "lvlOne":
        lvlOne()
        eh.output.one.on()

    elif currentlvl == "lvlTwo":
        lvlTwo()
        eh.output.one.off()
        eh.output.two.on()

    elif currentlvl == "lvlThree":
        lvlThree()
        eh.output.two.off()
        eh.output.three.on()

    elif currentlvl == "endScreen":
        endScreen()
       
        eh.output.one.on()
        eh.output.two.on()
        eh.output.three.on()

    elif currentlvl == "jumpscare":
        menuBackground.fill((0,0,0))
        jumpScare()
       
        eh.output.one.off()
        eh.output.two.off()
        eh.output.three.off()

        goatScream.play()
       

    cursor.update()

    menuBackground.blit(cursor.image, pygame.mouse.get_pos())

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:

             if currentlvl == "menu":

                if 265 <= mouse[0] <= 365 and 350 <= mouse[1] <= 390:

                    black = (0,0,0)
                    menuBackground.fill(black)
                    currentlvl = "lvlOne"


             elif currentlvl == "endScreen":
                if 220 <= mouse[0] <= 410 and 525 <= mouse[1] <= 565:
                    menuBackground.fill(aqua)
                    currentlvl = "menu"

             elif currentlvl == "jumpscare":
                 if 1 <= mouse[0]<= 625 and 1 <= mouse[1] <= 600:
                     menuBackground.fill(aqua)
                     currentlvl = "menu"

        if event.type == MOUSEMOTION:

            if currentlvl == "lvlOne":
                menuBackground.fill((0, 0, 0))  # Black color
               
                lvlOne()
               
                eh.output.one.on()

                path = pygame.draw.rect(menuBackground, aqua, pygame.Rect(220,45,260,50))
                path2 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(220,90,150,400))
                end = pygame.draw.rect(menuBackground, red, pygame.Rect(450,45,80,50))

                collide1 = pygame.Rect.colliderect(cursor.rect, path)
                collide2 = pygame.Rect.colliderect(cursor.rect, path2)
                collideEnd = pygame.Rect.colliderect(cursor.rect, end)

                if collideEnd:
                    menuBackground.fill(black)
                    currentlvl = "lvlTwo"
                    lvlTwo()

                elif collide1 or collide2:
                    print("On path")

                else:
                    currentlvl = "jumpscare"

            elif currentlvl == "lvlTwo":
               
                menuBackground.fill((0,0,0))
               
                eh.output.one.off()
                eh.output.two.on()
               
                lvl2p = pygame.draw.rect(menuBackground, aqua, pygame.Rect(150,45,370,50))
                lvl2p2 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,45,50,90))
                lvl2p3 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,135,430,50))
                lvl2p4 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(480,165,50,90))
                lvl2p5 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,225,430,50))
                lvl2p6 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,235,50,90))
                lvl2p7 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,315,430,50))
                lvl2p8 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(460,315,70,110))
                lvl2p9 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,395,430,40))
                lvl2End = pygame.draw.rect(menuBackground, red, pygame.Rect(100,395,80,40))

                menuBackground.blit(cursor.image, pygame.mouse.get_pos())

                collision1 = pygame.Rect.colliderect(cursor.rect, lvl2p)
                collision2 = pygame.Rect.colliderect(cursor.rect, lvl2p2)
                collision3 = pygame.Rect.colliderect(cursor.rect, lvl2p3)
                collision4 = pygame.Rect.colliderect(cursor.rect, lvl2p4)
                collision5 = pygame.Rect.colliderect(cursor.rect, lvl2p5)
                collision6 = pygame.Rect.colliderect(cursor.rect, lvl2p6)
                collision7 = pygame.Rect.colliderect(cursor.rect, lvl2p7)
                collision8 = pygame.Rect.colliderect(cursor.rect, lvl2p8)
                collision9 = pygame.Rect.colliderect(cursor.rect, lvl2p9)
                collisionEnded = pygame.Rect.colliderect(cursor.rect, lvl2End)

                if collisionEnded:
                    currentlvl = "lvlThree"
                    lvlThree()

                elif collision1 or collision2 or collision3 or collision4 or collision5 or collision6 or collision7 or collision8 or collision9:
                    print("On path")

                else:
                    currentlvl = "jumpscare"


            elif currentlvl =="lvlThree":
               
                menuBackground.fill((0,0,0))
               
                eh.output.two.off()
                eh.output.three.on()

                p1 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,395,430,40))
                p2 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(490,355,40,60))
                p3 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,335,430,40))
                p4 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,275,40,60))
                p5 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,235,140,50))
                p6 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(100,235,300,20))
                p7 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(400,195, 20, 60))
                p8 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(280,195,120,20))
                p9 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(315,80,20,65))
                p10 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(260,145,20,70))
                p11 = pygame.draw.rect(menuBackground, aqua, pygame.Rect(260,145,75,20))
                pEnd = pygame.draw.rect(menuBackground, red, pygame.Rect(300,35,50,70))

                collides = pygame.Rect.colliderect(cursor.rect, p1)
                collides2 = pygame.Rect.colliderect(cursor.rect, p2)
                collides3 = pygame.Rect.colliderect(cursor.rect, p3)
                collides4 = pygame.Rect.colliderect(cursor.rect, p4)
                collides5 = pygame.Rect.colliderect(cursor.rect, p5)
                collides6 = pygame.Rect.colliderect(cursor.rect, p6)
                collides7 = pygame.Rect.colliderect(cursor.rect, p7)
                collides8 = pygame.Rect.colliderect(cursor.rect, p8)
                collides9 = pygame.Rect.colliderect(cursor.rect, p9)
                collides10 = pygame.Rect.colliderect(cursor.rect, p10)
                collides11 = pygame.Rect.colliderect(cursor.rect, p11)
                collidesEnded = pygame.Rect.colliderect(cursor.rect, pEnd)

                if collidesEnded:
                    menuBackground.fill((0,0,0))
                    currentlvl = "endScreen"
                   
                    eh.output.one.on()
                    eh.output.two.on()
                    eh.output.three.on()

                elif collides or collides2 or collides3 or collides4 or collides5 or collides6 or collides7 or collides8 or collides9 or collides10 or collides11:
                    print("On path")

                else:
                    currentlvl = "jumpscare"
                   
                    eh.output.one.off()
                    eh.output.two.off()
                    eh.output.three.off()
   
    pygame.display.update()