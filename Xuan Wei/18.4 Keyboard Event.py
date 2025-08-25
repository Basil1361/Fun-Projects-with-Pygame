import pygame, sys, time
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((900, 600))

    myFont = pygame.font.Font("arialunicodems.ttf", 50)
    yellow = (255, 255, 0)
    blue = (0, 0, 200)

    text = "Testing keyboard"

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.fill(blue)
        textImage = myFont.render(text, True, yellow)
        screen.blit(textImage, (50, 200))
        keys = pygame.key.get_pressed()

        if keys[K_ESCAPE]:
            sys.exit()
        if keys[K_SPACE]:
            text = "Key pressed: SPACE"
        if keys[K_RETURN]:
            text = "Key pressed: ENTER"

        time.sleep(1/60)
        pygame.display.update()