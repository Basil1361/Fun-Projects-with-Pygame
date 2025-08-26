#在窗⼝上绘制⼀个指针时钟（带时针、分针和秒针），并在窗⼝左上⻆以数字形式显⽰当前时间，效果如图18-14所⽰。

import pygame, sys, time
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Adding Graphics")

    myFont = pygame.font.Font("arialunicodems.ttf", 30)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    blue = (0, 0, 200)
    white = (255, 255, 255)
    black = (0, 0, 0)

    #19.1.1 Adding background photo
    lantern_bg = pygame.image.load("Resources/Image/Lantern_rite_bg.png").convert_alpha()
    scaled_lantern_bg = pygame.transform.smoothscale(lantern_bg, (1200, 700))
    screen.blit(scaled_lantern_bg, (0, 0))

    #19.1.2 Adding graphics objects
    xiao1_img = pygame.image.load("Resources/Image/xiao1_image.png").convert_alpha()
    scaled_xiao1_img = pygame.transform.smoothscale(xiao1_img, (200, 200))
    screen.blit(scaled_xiao1_img, (400, 400))

    zhongli1_img = pygame.image.load("Resources/Image/zhongli1_image.png").convert_alpha()
    scaled_zhongli1_img = pygame.transform.smoothscale(zhongli1_img, (250, 250))
    screen.blit(scaled_zhongli1_img, (600, 350))

    pygame.display.update()

    def showText(font, x, y, text, color=(255, 255, 255)):
        textImage = font.render(text, True, color)
        screen.blit(textImage, (x, y))


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()

        time.sleep(0.5)
