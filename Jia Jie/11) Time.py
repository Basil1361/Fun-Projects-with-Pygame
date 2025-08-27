#  Creating a timer

import pygame as pg
from sys import exit    


pg.init()
screen = pg.display.set_mode((800, 400), pg.RESIZABLE)
pg.display.set_caption("Image Display")
clock = pg.time.Clock()
link = "D:\Pygame\Jia Jie\InputFiles\Font\Pixeltype.ttf"
font = pg.font.Font(link,50)

# background
sky_surf = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\Sky.png").convert_alpha()
ground_surf = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\ground.png").convert_alpha()
color = (64,64,64)
text_surf = font.render("Game", True, color)
text_rect = text_surf.get_rect(center = (400, 50))

# snail
snail_surf = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\snail\snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

# colour
colorhex = "#c0ec8d"

# player
player_surf = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\player\player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(bottomright = (80, 300))
player_gravity = 0
key = pg.key.get_pressed()

# game state 
game_state = True
game_time = 0

def timer():
    default = pg.time.get_ticks() - game_time
    current = default/1000
    time_surf = font.render(f'{current:.0f}',False,20)
    # render(string, False, 20)
    # current is a float, formatted with :.0f to show no decimal places
    time_rect = time_surf.get_rect(center = (400,50))
    screen.blit(time_surf,time_rect)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if game_state:
            if event.type == pg.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20  
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and player_rect.bottom == 300:
                player_gravity = -20  
        else:
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                game_state = True
                snail_rect.left = 800
                game_time = pg.time.get_ticks()  # Reset timer to current time for zero start

    if game_state:
    # background
        screen.blit(sky_surf,(0, 0))
        screen.blit(ground_surf,(0, 300))
        # pg.draw.rect(screen, colorhex ,text_rect)
        # pg.draw.rect(screen, colorhex ,text_rect, 10)
        # screen.blit(text_surf,text_rect)
        # moving sprite 
        snail_rect.x -= 4
        if snail_rect.right <= 0: 
            snail_rect.left = 800 

        # gravity
        player_gravity += 1
        player_rect.y += player_gravity
        
        # keep player on ground
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
            player_gravity = 0
        
        # sprites
        screen.blit(snail_surf, snail_rect)
        screen.blit(player_surf, player_rect)
        
        # time
        timer()
    
    # collision / quit
        if player_rect.colliderect(snail_rect):
            game_state = False
            
    else:
        screen.fill("Black")
    
    pg.display.update()
    clock.tick(60)
