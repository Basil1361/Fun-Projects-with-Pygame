import pygame, sys, time
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Moving Graphics")

    myFont = pygame.font.Font("arialunicodems.ttf", 30)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    blue = (0, 0, 200)
    white = (255, 255, 255)
    black = (0, 0, 0)


    false_sky_bg = pygame.image.load("Resources/Image/False_Sky_image.png").convert_alpha()
    scaled_false_sky_bg = pygame.transform.smoothscale(false_sky_bg, (1200, 700))

    earth_img = pygame.image.load("Resources/Image/Earth_image.png").convert_alpha()
    scaled_earth_img = pygame.transform.smoothscale(earth_img, (600, 600))


    def showText(font, x, y, text, color=(255, 255, 255)):
        textImage = font.render(text, True, color)
        screen.blit(textImage, (x, y))

    angle = 0.0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        angle += 0.5
        if angle >= 360:
            angle = 0.0

        rotated_earth_img = pygame.transform.rotate(scaled_earth_img, angle)
        rotated_rect = rotated_earth_img.get_rect(center=scaled_earth_img.get_rect(center=(600, 350)).center)

        screen.blit(scaled_false_sky_bg, (0, 0))
        screen.blit(rotated_earth_img, rotated_rect.topleft)

        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()

        time.sleep(1/60)
        pygame.display.update()
