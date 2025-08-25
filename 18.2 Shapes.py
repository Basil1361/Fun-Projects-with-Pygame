import pygame, sys, math
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((900, 600))

    red = (255, 0, 0)
    yellow = (255, 255, 0)
    blue = (0, 0, 200)
    green = (0, 200, 0)

    screen.fill(blue)

    #18.2.1 Circle
    #circle(surface, color, center, radius, width=0)
    pygame.draw.circle(screen, yellow, (100, 100), 40, 5)

    #18.2.2 Rectangle
    #rect(surface, color, rect, width=0)
    pygame.draw.rect(screen, red, (200, 200, 50, 50), 0)

    #18.2.3 Line
    #line(surface, color, start_pos, end_pos, width=1)
    pygame.draw.line(screen, yellow, (300, 250), (500, 500), 5)

    #18.2.4 Arc
    #arc(surface, color, rect, start_angle, stop_angle, width=1)
    pygame.draw.arc(screen, yellow, (600, 400, 150, 150), math.pi, math.pi*2, 5)

    pygame.display.update()

    typeList = [QUIT]
    while True:
        for event in pygame.event.get():
            if event.type in typeList:
                sys.exit()