import pygame
from pygame.locals import QUIT

pygame.init()

res2 = (720,720)
menuBackground = pygame.display.set_mode(res2)

black = (0,0,0)
menuBackground.fill(black)


pygame.mouse.set_visible(False)

aqua = (1, 255, 255)
red = (255,0,0)

pygame.draw.rect(menuBackground, aqua, pygame.Rect(200,45,300,50))
pygame.draw.rect(menuBackground, aqua, pygame.Rect(200,90,150,400))
pygame.draw.rect(menuBackground, red, pygame.Rect(450,45,80,50))


class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("square (1).jpg")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

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
    
run = True
mouse = Cursor()

while run:

    menuBackground.fill(black)
    mouse.update()

    path = pygame.draw.rect(menuBackground, aqua, pygame.Rect(200,45,250,50))
    path2= pygame.draw.rect(menuBackground, aqua, pygame.Rect(200,90,150,400))
    end = pygame.draw.rect(menuBackground, red, pygame.Rect(450,45,80,50))

    menuBackground.blit(mouse.image, pygame.mouse.get_pos())
    
    collide1 = False
    collide2 = False
    collideEnd = False

    collide1 = pygame.Rect.colliderect(mouse.rect, path)
    collide2 = pygame.Rect.colliderect(mouse.rect, path2)
    collideEnd = pygame.Rect.colliderect(mouse.rect, end)

    if collideEnd:
        menuBackground.fill(black)
        lvlTwo()

    elif collide1 or collide2:
        print("On path")

    else:
        print("Off path")
        
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False


    pygame.display.update()

pygame.quit()