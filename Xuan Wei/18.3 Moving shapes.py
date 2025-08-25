import pygame, sys, time
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((900, 600))

    red = (255, 0, 0)
    yellow = (255, 255, 0)
    blue = (0, 0, 200)

    myFont = pygame.font.Font("arialunicodems.ttf", 50)
    textImage = myFont.render("你好 / ありがとう / Hello Pygame", True, yellow)
    
    x_coor = 200
    y_coor = 300
    dx = 2
    dy = 1.5

    while True:
        screen.fill(blue)
        screen.blit(textImage, (50, 200))
        x_coor += dx
        y_coor += dy
        if x_coor < 0 or x_coor > 850:
            dx = -dx
        if y_coor < 0 or y_coor > 550:
            dy = -dy
        pygame.draw.rect(screen, red, (x_coor, y_coor, 50, 50), 0)
        time.sleep(0.01)
        pygame.display.update()

        typeList = [QUIT]
        for event in pygame.event.get():
            if event.type in typeList:
                sys.exit()