import pygame, sys
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((900, 600))

    myFont = pygame.font.Font("arialunicodems.ttf", 50)
    yellow = (255, 255, 0)
    blue = (0, 0, 200)
    textImage = myFont.render("你好 / ありがとう / Hello Pygame", True, yellow)

    screen.fill(blue)
    screen.blit(textImage, (50, 200))

    pygame.display.update()

    typeList = [QUIT]
    while True:
        for event in pygame.event.get():
            if event.type in typeList:
                sys.exit()