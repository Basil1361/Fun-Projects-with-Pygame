#在窗⼝上绘制⼀个指针时钟（带时针、分针和秒针），并在窗⼝左上⻆以数字形式显⽰当前时间，效果如图18-14所⽰。

import pygame, sys, time, math
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((900, 600))

    myFont = pygame.font.Font("arialunicodems.ttf", 30)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    blue = (0, 0, 200)
    white = (255, 255, 255)
    black = (0, 0, 0)

    def showText(font, x, y, text, color=(255, 255, 255)):
        textImage = font.render(text, True, color)
        screen.blit(textImage, (x, y))


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.fill(black)
        pygame.draw.circle(screen, white, (450, 300), 250, 5)

        for i in range(1, 13):
            showText(myFont, 440 + 210 * math.sin(math.pi * i / 6), 280 - 210 * math.cos(math.pi * i / 6), str(i))


        local_time = time.localtime()
        showText(myFont,10, 10, f"{str(time.strftime("%H:%M:%S", local_time))} (UTC+8)")

        minute = int(time.strftime("%M", local_time))
        minute_end_x_coor = 450 + 200 * math.sin(math.pi * minute / 30)
        minute_end_y_coor = 300 - 200 * math.cos(math.pi * minute / 30)
        pygame.draw.line(screen, white, (450, 300), (minute_end_x_coor, minute_end_y_coor), 8)

        hour = int(time.strftime("%H", local_time))
        hour_end_x_coor = 450 + 160 * math.sin(math.pi * (hour / 6 + minute / 360))
        hour_end_y_coor = 300 - 160 * math.cos(math.pi * (hour / 6 + minute / 360))
        pygame.draw.line(screen, white, (450, 300), (hour_end_x_coor, hour_end_y_coor), 10)

        second = int(time.strftime("%S", local_time))
        second_end_x_coor = 450 + 225 * math.sin(math.pi * second / 30)
        second_end_y_coor = 300 - 225 * math.cos(math.pi * second / 30)
        pygame.draw.line(screen, red, (450, 300), (second_end_x_coor, second_end_y_coor), 2)

        pygame.draw.circle(screen, white, (450, 300), 15, 0)


        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()


        pygame.display.update()
        time.sleep(0.5)
