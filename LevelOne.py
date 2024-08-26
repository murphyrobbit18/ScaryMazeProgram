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

pygame.draw.rect(levelOne, aqua, pygame.Rect(200,45,300,50))
pygame.draw.rect(levelOne, aqua, pygame.Rect(200,90,150,400))
pygame.draw.rect(levelOne, red, pygame.Rect(450,45,80,50))
while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
pygame.display.update()