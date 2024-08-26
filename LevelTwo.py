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

pygame.draw.rect(levelOne, aqua, pygame.Rect(150,45,370,50))
pygame.draw.rect(levelOne, aqua, pygame.Rect(100,45,50,90))
pygame.draw.rect(levelOne, aqua, pygame.Rect(100,135,430,50))
pygame.draw.rect(levelOne, aqua, pygame.Rect(480,165,50,90))
pygame.draw.rect(levelOne, aqua, pygame.Rect(100,225,430,50))
pygame.draw.rect(levelOne, aqua, pygame.Rect(100,235,50,90))
pygame.draw.rect(levelOne, aqua, pygame.Rect(100,315,430,50))
pygame.draw.rect(levelOne, aqua, pygame.Rect(460,315,70,110))
pygame.draw.rect(levelOne, aqua, pygame.Rect(100,395,430,40))
pygame.draw.rect(levelOne, red, pygame.Rect(100,395,80,40))

while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
pygame.display.update()