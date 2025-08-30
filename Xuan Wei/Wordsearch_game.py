import pygame, sys, time
from pygame.locals import *


def run_game(order, words, crossword, arrangements, audio, theme):
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

    dragging = False
    quit_rect = pygame.Rect(1050, 0, 150, 50)
    click_to_quit = False
    start_pos = (0, 0)
    end_pos = (0, 0)

    initial_width = 50
    initial_height = (830 - order * 45) // 2

    arrangements_in_coor = []
    for i, j, k in arrangements:
        start_x_coor = initial_width + 45*j[1] + 23
        start_y_coor = initial_height + 45*j[0] + 23
        end_x_coor = initial_width + 45*k[1] + 23
        end_y_coor = initial_height + 45*k[0] + 23
        arrangements_in_coor.append([i, (start_x_coor, start_y_coor), (end_x_coor, end_y_coor), False])

    words = sorted(words, key=len, reverse=True)
    remaining_words = words
    total_words = len(words)






    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    dragging = True
                    down_start_pos = event.pos
                    down_end_pos = event.pos
                    mouseDownX, mouseDownY = event.pos
                    if quit_rect.collidepoint(down_start_pos):
                        click_to_quit = True


            elif event.type == MOUSEBUTTONUP:
                up_pos = event.pos
                if event.button == 1:
                    dragging = False
                    mouseUpX, mouseUpY = event.pos
                    if quit_rect.collidepoint(up_pos) and click_to_quit:
                        pygame.quit()
                        sys.exit
                click_to_quit = False

            elif event.type == MOUSEMOTION and dragging:
                down_end_pos = event.pos

        screen.fill(black)

        showText(myFont, 1030, 750, f"({str(mouseDownX)}, {str(mouseDownY)})", white)
        showText(myFont, 1030, 780, f"({str(mouseUpX)}, {str(mouseUpY)})")


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

        for index, word in enumerate(words):
            word = word.upper()
            showText(myFont, 950, 75+index*35, word, white)


        pygame.draw.rect(screen, blue, (1050, 0, 150, 50), 0)
        showText(myFont, 1070, 0, "< Return", white)



        if dragging:
            pygame.draw.line(screen, yellow, down_start_pos, down_end_pos, 1)

        for x in arrangements_in_coor:
            if (x[1][0]-23<mouseDownX<x[1][0]+23 and x[1][1]-23<mouseDownY<x[1][1]+23
                    and x[2][0]-23<mouseUpX<x[2][0]+23 and x[2][1]-23<mouseUpY<x[2][1]+23):
                x[3] = True

        count = 0
        for y in arrangements_in_coor:
            if y[3]:
                pygame.draw.line(screen, yellow, y[1], y[2], 1)
                pygame.draw.line(screen, yellow, (940, 75+ arrangements_in_coor.index(y)*35 +22),
                                 (1150, 75+ arrangements_in_coor.index(y)*35 +22), 1)
                count += 1

        if count == total_words:
            pygame.draw.rect(screen, black, (200, 200, 800, 430), 0)
            showText(myFont, 400, 400, "GAME OVER", white)

        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()

        time.sleep(1/60)
        pygame.display.update()


if __name__ == "__main__":
    puzzle = [['P', 'S', 'K', 'O', 'S', 'Q', 'Q', 'D', 'R', 'K', 'K', 'G', 'E', 'Z', 'Z', 'B', 'P'],
['D', 'C', 'K', 'G', 'C', 'U', 'C', 'U', 'M', 'B', 'E', 'R', 'B', 'W', 'Q', 'Y', 'G'],
['W', 'H', 'X', 'B', 'D', 'R', 'C', 'H', 'O', 'P', 'S', 'T', 'I', 'C', 'K', 'S', 'K'],
['P', 'K', 'V', 'T', 'L', 'G', 'V', 'O', 'D', 'P', 'M', 'S', 'R', 'C', 'N', 'T', 'S'],
['C', 'Z', 'E', 'T', 'H', 'N', 'I', 'C', 'I', 'T', 'Y', 'A', 'O', 'F', 'E', 'Z', 'V'],
['O', 'Q', 'Y', 'F', 'D', 'B', 'N', 'W', 'Z', 'V', 'Q', 'X', 'F', 'D', 'F', 'Y', 'G'],
['L', 'P', 'K', 'X', 'F', 'Q', 'M', 'M', 'A', 'C', 'R', 'H', 'E', 'K', 'K', 'Y', 'Z'],
['L', 'X', 'T', 'Y', 'W', 'A', 'M', 'X', 'L', 'T', 'C', 'K', 'H', 'H', 'M', 'E', 'Z'],
['I', 'D', 'D', 'H', 'B', 'A', 'Z', 'B', 'D', 'Q', 'W', 'Q', 'W', 'C', 'X', 'D', 'L'],
['S', 'G', 'E', 'A', 'H', 'C', 'Y', 'N', 'N', 'G', 'I', 'H', 'G', 'L', 'M', 'I', 'R'],
['I', 'I', 'S', 'R', 'H', 'F', 'C', 'A', 'T', 'T', 'E', 'M', 'P', 'T', 'M', 'T', 'B'],
['O', 'M', 'E', 'C', 'T', 'K', 'X', 'A', 'Z', 'J', 'P', 'E', 'J', 'Y', 'U', 'H', 'R'],
['N', 'B', 'R', 'I', 'N', 'K', 'C', 'X', 'K', 'I', 'N', 'L', 'Q', 'H', 'O', 'Q', 'Z'],
['K', 'Q', 'T', 'T', 'N', 'E', 'Q', 'P', 'L', 'X', 'V', 'I', 'G', 'U', 'R', 'L', 'T'],
['F', 'P', 'E', 'O', 'G', 'Q', 'M', 'D', 'B', 'A', 'M', 'E', 'C', 'C', 'A', 'Z', 'Z'],
['D', 'I', 'D', 'H', 'W', 'K', 'R', 'E', 'S', 'E', 'R', 'V', 'O', 'I', 'R', 'V', 'A'],
['W', 'W', 'N', 'V', 'I', 'O', 'L', 'A', 'T', 'I', 'O', 'N', 'X', 'H', 'G', 'X', 'R']]
    words = ['brink', 'deserted', 'mecca', 'reservoir', 'chopsticks', 'tempt', 'violation', 'collision', 'ethnicity', 'cucumber']
             #, ['apple', 'banana', 'chameleon', 'dandeleon', 'eerie', 'furious', 'granny', 'hinge', 'illuminate', 'joke']
    arrangement = [('CHOPSTICKS', (2, 6), (2, 15)), ('RESERVOIR', (15, 6), (15, 14)), ('VIOLATION', (16, 3), (16, 11)),
     ('COLLISION', (4, 0), (12, 0)), ('ETHNICITY', (4, 2), (4, 10)), ('DESERTED', (8, 2), (15, 2)),
     ('CUCUMBER', (1, 4), (1, 11)), ('BRINK', (12, 1), (12, 5)), ('MECCA', (14, 10), (14, 14)),
     ('TEMPT', (10, 9), (10, 13))]
    run_game(17, words, puzzle, arrangement, "None", "Black")
