import pygame, sys, time
from pygame.locals import *


def run_game(order, crossword, audio, theme):
    pygame.init()
    screen = pygame.display.set_mode((1200, 830))
    pygame.display.set_caption("Wordsearch Puzzle - Game")

    def showText(font, x, y, text, color=(255, 255, 255)):
        textImage = font.render(text, True, color)
        screen.blit(textImage, (x, y))

    myFont = pygame.font.Font("arialunicodems.ttf", 30)
    crosswordFont = pygame.font.Font("arialunicodems.ttf", 20)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    blue = (0, 0, 200)
    white = (230, 230, 230)
    black = (50, 50, 50)


    mouseX = mouseY = moveX = moveY = mouseDown = mouseUp = mouseDownX = mouseDownY = mouseUpX = mouseUpY = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
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

        screen.fill(black)

        initial_width = 50
        initial_height = (830 - order*45) // 2
        for i in range (order + 1):
            pygame.draw.line(screen, white, (initial_width, initial_height + 45*i),
                             (initial_width + 45*(order), initial_height + 45*i), 1) #Horizontal
            pygame.draw.line(screen, white, (initial_width + 45*i, initial_height),
                             (initial_width + 45*i, initial_height + 45*(order)), 1) #Vertical

        for index, char_list in enumerate(crossword):
            for char_index, char in enumerate(char_list):
                showText(myFont, initial_width+10 + 45*char_index, initial_height + 45*index, char, white)







        pygame.draw.rect(screen, blue, (1050, 0, 150, 50), 0)
        showText(myFont, 1070, 0, "< Return", white)

        x, y = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()

        quit_cond = False
        if 1050<x<1200 and 0<y<50 and b1 == True:
            quit_cond = True
        if quit_cond:
            sys.exit()



        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()

        time.sleep(1/60)
        pygame.display.update()


if __name__ == "__main__":
    puzzle = [['K', 'F', 'E', 'N', 'D', 'V', 'P', 'X', 'Q', 'J', 'F', 'M', 'P', 'C', 'K', 'M', 'N'],
              ['N', 'I', 'E', 'Q', 'L', 'N', 'N', 'T', 'M', 'G', 'N', 'L', 'K', 'M', 'T', 'F', 'R'],
              ['D', 'J', 'O', 'M', 'W', 'B', 'K', 'C', 'B', 'S', 'E', 'M', 'A', 'J', 'F', 'M', 'R'],
              ['T', 'W', 'A', 'V', 'C', 'H', 'A', 'M', 'E', 'L', 'E', 'O', 'N', 'F', 'O', 'R', 'P'],
              ['W', 'C', 'D', 'B', 'A', 'N', 'A', 'N', 'A', 'A', 'O', 'T', 'D', 'S', 'F', 'X', 'W'],
              ['B', 'W', 'J', 'C', 'W', 'X', 'V', 'B', 'Q', 'P', 'Y', 'Y', 'Q', 'P', 'D', 'O', 'U'],
              ['A', 'U', 'J', 'B', 'R', 'S', 'H', 'C', 'G', 'R', 'Q', 'R', 'A', 'M', 'X', 'K', 'J'],
              ['P', 'W', 'L', 'P', 'Q', 'V', 'M', 'G', 'Q', 'S', 'N', 'F', 'E', 'E', 'T', 'Y', 'U'],
              ['P', 'R', 'N', 'O', 'T', 'A', 'J', 'M', 'O', 'G', 'M', 'J', 'Y', 'G', 'K', 'I', 'C'],
              ['L', 'D', 'N', 'H', 'X', 'U', 'U', 'S', 'Q', 'D', 'O', 'U', 'J', 'U', 'B', 'F', 'F'],
              ['E', 'P', 'J', 'R', 'B', 'E', 'Y', 'Z', 'B', 'S', 'X', 'W', 'T', 'E', 'D', 'H', 'N'],
              ['H', 'L', 'C', 'S', 'N', 'F', 'A', 'N', 'G', 'U', 'P', 'S', 'R', 'J', 'F', 'W', 'Y'],
              ['S', 'C', 'C', 'J', 'H', 'J', 'R', 'F', 'Q', 'U', 'P', 'C', 'S', 'L', 'B', 'U', 'B'],
              ['Q', 'W', 'W', 'C', 'E', 'N', 'F', 'Y', 'Y', 'G', 'K', 'O', 'X', 'X', 'I', 'R', 'H'],
              ['P', 'Q', 'S', 'F', 'Q', 'P', 'K', 'X', 'E', 'A', 'R', 'O', 'M', 'G', 'X', 'Y', 'C'],
              ['N', 'B', 'Q', 'N', 'D', 'G', 'D', 'P', 'C', 'C', 'B', 'O', 'S', 'B', 'I', 'D', 'G'],
              ['L', 'K', 'O', 'F', 'N', 'P', 'F', 'S', 'T', 'A', 'A', 'N', 'F', 'G', 'L', 'F', 'T']]
    run_game(17, puzzle, "None", "Black")