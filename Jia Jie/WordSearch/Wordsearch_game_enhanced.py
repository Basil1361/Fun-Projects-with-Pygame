import pygame, sys, time, math
from pygame.locals import *


def run_game(order, words, crossword, arrangements, audio, theme):
    pygame.init()
    screen = pygame.display.set_mode((1200, 830))
    pygame.display.set_caption("Wordsearch Puzzle - Game")

    def showText(font, x, y, text, color=(255, 255, 255)):
        textImage = font.render(text, True, color)
        screen.blit(textImage, (x, y))

    # Fonts and colors
    myFont = pygame.font.Font(None, 30)
    crosswordFont = pygame.font.Font(None, 20)
    congratsFont = pygame.font.Font(None, 48)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    blue = (0, 0, 200)
    white = (230, 230, 230)
    black = (50, 50, 50)
    green = (0, 255, 0)
    lightgray = (150, 150, 150)

    # Mouse and game state variables
    mouseX = mouseY = moveX = moveY = mouseDown = mouseUp = mouseDownX = mouseDownY = mouseUpX = mouseUpY = 0
    dragging = False
    quit_rect = pygame.Rect(1050, 0, 150, 50)
    click_to_quit = False
    
    # Grid positioning
    initial_width = 50
    initial_height = (830 - order * 45) // 2

    # Convert arrangements to coordinate system
    arrangements_in_coor = []
    for i, j, k in arrangements:
        start_x_coor = initial_width + 45*j[1] + 23
        start_y_coor = initial_height + 45*j[0] + 23
        end_x_coor = initial_width + 45*k[1] + 23
        end_y_coor = initial_height + 45*k[0] + 23
        arrangements_in_coor.append((i, (start_x_coor, start_y_coor), (end_x_coor, end_y_coor), j, k))

    # Track found words
    found_words = set()
    found_lines = []
    game_completed = False
    congrats_timer = 0
    
    def check_word_selection(start_pos, end_pos):
        """Check if the selection matches any word in the puzzle"""
        tolerance = 23  # Allow some tolerance for clicking
        
        for word, start_coord, end_coord, start_grid, end_grid in arrangements_in_coor:
            if word in found_words:
                continue
                
            # Check if selection matches word (either direction)
            start_match1 = (abs(start_pos[0] - start_coord[0]) <= tolerance and 
                           abs(start_pos[1] - start_coord[1]) <= tolerance)
            end_match1 = (abs(end_pos[0] - end_coord[0]) <= tolerance and 
                         abs(end_pos[1] - end_coord[1]) <= tolerance)
            
            start_match2 = (abs(start_pos[0] - end_coord[0]) <= tolerance and 
                           abs(start_pos[1] - end_coord[1]) <= tolerance)
            end_match2 = (abs(end_pos[0] - start_coord[0]) <= tolerance and 
                         abs(end_pos[1] - start_coord[1]) <= tolerance)
            
            if (start_match1 and end_match1) or (start_match2 and end_match2):
                found_words.add(word)
                found_lines.append((start_coord, end_coord))
                return word
        return None

    def check_game_completion():
        """Check if all words have been found"""
        return len(found_words) == len(words)

    # Main game loop
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
                    
                    # Check if this selection matches a word
                    if not game_completed:
                        found_word = check_word_selection(down_start_pos, up_pos)
                        if found_word:
                            print(f"Found word: {found_word}")
                            
                        # Check if game is completed
                        if check_game_completion():
                            game_completed = True
                            congrats_timer = pygame.time.get_ticks()
                    
                    if quit_rect.collidepoint(up_pos) and click_to_quit:
                        pygame.quit()
                        sys.exit()
                click_to_quit = False

            elif event.type == MOUSEMOTION and dragging:
                down_end_pos = event.pos

        # Clear screen
        screen.fill(black)

        # Draw grid
        for i in range(order + 1):
            pygame.draw.line(screen, white, (initial_width, initial_height + 45*i),
                             (initial_width + 45*(order), initial_height + 45*i), 1)  # Horizontal
            pygame.draw.line(screen, white, (initial_width + 45*i, initial_height),
                             (initial_width + 45*i, initial_height + 45*(order)), 1)  # Vertical

        # Draw letters
        for index, char_list in enumerate(crossword):
            for char_index, char in enumerate(char_list):
                showText(myFont, initial_width+10 + 45*char_index, initial_height + 45*index, char, white)

        # Draw word list with different colors for found/unfound words
        for index, word in enumerate(words):
            word_upper = word.upper()
            color = green if word_upper in found_words else white
            showText(myFont, 950, 75+index*35, word_upper, color)

        # Draw found word lines
        for start_coord, end_coord in found_lines:
            pygame.draw.line(screen, green, start_coord, end_coord, 3)

        # Draw current selection line
        if dragging and not game_completed:
            pygame.draw.line(screen, yellow, down_start_pos, down_end_pos, 2)

        # Draw quit button
        pygame.draw.rect(screen, blue, (1050, 0, 150, 50), 0)
        showText(myFont, 1070, 0, "< Return", white)

        # Show congratulations message if game is completed
        if game_completed:
            current_time = pygame.time.get_ticks()
            # Show congratulations message indefinitely until user quits
            # Draw semi-transparent overlay
            overlay = pygame.Surface((1200, 830))
            overlay.set_alpha(180)
            overlay.fill(black)
            screen.blit(overlay, (0, 0))
            
            # Draw congratulations text with animation
            alpha = int(128 + 127 * abs(math.sin(current_time * 0.005)))  # Pulsing effect
            
            congrats_text = "CONGRATULATIONS!"
            completion_text = f"You found all {len(words)} words!"
            continue_text = "Press ESC to exit or click Return"
            
            # Create surfaces with pulsing effect
            congrats_surface = congratsFont.render(congrats_text, True, (255, alpha, 0))
            completion_surface = myFont.render(completion_text, True, white)
            continue_surface = myFont.render(continue_text, True, lightgray)
            
            # Center the text
            congrats_rect = congrats_surface.get_rect(center=(600, 350))
            completion_rect = completion_surface.get_rect(center=(600, 400))
            continue_rect = continue_surface.get_rect(center=(600, 450))
            
            screen.blit(congrats_surface, congrats_rect)
            screen.blit(completion_surface, completion_rect)
            screen.blit(continue_surface, continue_rect)

        # Handle escape key
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()

        time.sleep(1/60)
        pygame.display.update()


if __name__ == "__main__":
    # Test data
    puzzle = [['P', 'S', 'K', 'O', 'S', 'Q', 'Q', 'D', 'R', 'K', 'K', 'G', 'E', 'Z', 'Z', 'B', 'P'],
              ['D', 'C', 'K', 'G', 'C', 'U', 'C', 'U', 'M', 'B', 'E', 'R', 'B', 'W', 'Q', 'Y', 'G']]
    words = ['CUCUMBER']
    arrangement = [('CUCUMBER', (1, 4), (1, 11))]
    run_game(17, words, puzzle, arrangement, "None", "Black")
