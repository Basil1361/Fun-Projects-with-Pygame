import pygame, sys, time
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((900, 600))

    myFont = pygame.font.Font("arialunicodems.ttf", 50)
    yellow = (255, 255, 0)
    blue = (0, 0, 200)

    def showText(font, x, y, text, color=(255, 255, 255)):
        textImage = font.render(text, True, color)
        screen.blit(textImage, (x, y))

    mouseX = mouseY = moveX = moveY = mouseDown = mouseUp = mouseDownX = mouseDownY = mouseUpX = mouseUpY = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos
                moveX, moveY = event.rel
            elif event.type == MOUSEBUTTONDOWN:
                mouseDown = event.button
                mouseDownX, mouseDownY = event.pos
            elif event.type == MOUSEBUTTONUP:
                mouseUp = event.button
                mouseUpX, mouseUpY = event.pos

        screen.fill(blue)

        showText(myFont, 20, 10, f"Mouse pos: {str(mouseX)}, {str(mouseY)}")
        showText(myFont, 20, 50, f"Mouse abs pos: {str(moveX)}, {str(moveY)}")
        showText(myFont, 20, 90, f"Mouse btn down: {str(mouseDown)} at {str(mouseDownX)}, {str(mouseDownY)}")
        showText(myFont, 20, 130, f"Mouse btn up: {str(mouseUp)} at {str(mouseUpX)}, {str(mouseUpY)}")

        x, y = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()

        text1 = f"Mouse pos: {x}, {y}"
        showText(myFont, 20, 300, text1)
        text2 = f"Mouse cond: {str(b1)}, {str(b2)}, {str(b3)}"
        showText(myFont, 20, 340, text2)

        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()

        time.sleep(1/60)
        pygame.display.update()