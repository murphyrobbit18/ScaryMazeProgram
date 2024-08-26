import pygame
from pygame.locals import QUIT
pygame.init()

res2 = (720,720)
screen = pygame.display.set_mode(res2)
levelOne = pygame.display.set_mode((625,600))

black = (0,0,0)
levelOne.fill(black)

aqua = (1, 255, 255)
red = (255,0,0)

pygame.draw.rect(levelOne, aqua, pygame.Rect(100,395,430,40))
pygame.draw.rect(levelOne, aqua, pygame.Rect(490,355,40,60))
pygame.draw.rect(levelOne, aqua, pygame.Rect(100,335,430,40))
pygame.draw.rect(levelOne, aqua, pygame.Rect(100,275,40,60))
pygame.draw.rect(levelOne, aqua, pygame.Rect(100,235,140,50))
pygame.draw.rect(levelOne, aqua, pygame.Rect(100,235,300,20))
pygame.draw.rect(levelOne, aqua, pygame.Rect(400,195, 20, 60))
pygame.draw.rect(levelOne, aqua, pygame.Rect(280,195,120,20))
pygame.draw.rect(levelOne, aqua, pygame.Rect(315,80,20,65))
pygame.draw.rect(levelOne, aqua, pygame.Rect(260,145,20,70))
pygame.draw.rect(levelOne, aqua, pygame.Rect(260,145,75,20))
pygame.draw.rect(levelOne, red, pygame.Rect(300,35,50,70))


while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
           
pygame.display.update()