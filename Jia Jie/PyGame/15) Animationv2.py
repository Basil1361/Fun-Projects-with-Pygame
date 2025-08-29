# Create a Custom Event
# Tell pygame to trigger that event continuously
# Add code in the event loop

# Part 2:
# Fix Collisions
# Delete list. 
# only one type of enemy. 

import pygame as pg
from sys import exit    
from random import randint


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

# snail + animation 
snail_surf = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\snail\snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))
obstacle_rect_list = []

# colour
colorhex = "#c0ec8d"

# player + animation (frame-to-frame)
player_walk1 = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\player\player_walk_1.png").convert_alpha()
player_walk2 = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\player\player_walk_2.png").convert_alpha()
player_walk = [player_walk1, player_walk2]
player_jump = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\Player\jump.png").convert_alpha()
player_index = 0
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(bottomright = (80, 300))
player_gravity = 0
key = pg.key.get_pressed()

# player stand
player_stand = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\Player\player_stand.png").convert_alpha()
# player_stand = pg.transform.scale2x(player_stand) -> 2x the original size
player_stand = pg.transform.rotozoom(player_stand, 0, 2)
# rotozoom parameters (surface, angle, size(scale))
player_stand_rect = player_stand.get_rect(center = (400,200))

# game state 
game_state = False
game_time = 0
game_name = font.render("Pixel Runner",False,(60,60,60))
game_name_rect = game_name.get_rect(center = (400,90))
game_message = font.render("Press Space to Start",False,(60,60,60))
game_message_rect = game_message.get_rect(center = (400,350))
score = 0 

# obstacle
obstacle_timer = pg.USEREVENT + 1
pg.time.set_timer(obstacle_timer, 1500)
# pg.time.set_timer((obstacle_timer), 900)

# fly + animation 
fly_surf = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\Fly\Fly1.png").convert_alpha()

def display_score():
    global current 
    default = pg.time.get_ticks() - game_time
    current = default/1000
    time_surf = font.render(f'{current:.0f}',False,20)
    # render(string, False, 20)
    # current is a float, formatted with :.0f to show no decimal places
    time_rect = time_surf.get_rect(center = (400,50))
    screen.blit(time_surf,time_rect)
    return int(current)  # Return the score as an integer

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5  # Move obstacles to the left
            
            # Determine which surface to blit based on obstacle position
            if obstacle_rect.bottom == 300:  # Ground obstacle (snail)
                screen.blit(snail_surf, obstacle_rect)
            else:  # Flying obstacle (fly)
                screen.blit(fly_surf, obstacle_rect)
            
        # Remove obstacles that have moved off screen
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
            
        return obstacle_list
    else:
        return []
            
def player_animation():
    global player_surf, player_index
    
    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1 
        if player_index >= len(player_walk): 
            player_index = 0
        player_surf = player_walk[int(player_index)]
        
    
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
                game_time = pg.time.get_ticks()  # Reset timer to current time for zero start
                obstacle_rect_list.clear()  # Clear obstacles when restarting
                
        if event.type == obstacle_timer and game_state:
            if randint(0,2):
                obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100),300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100),200)))
                
    if game_state:
    # background
        screen.blit(sky_surf,(0, 0))
        screen.blit(ground_surf,(0, 300))
        # pg.draw.rect(screen, colorhex ,text_rect)
        # pg.draw.rect(screen, colorhex ,text_rect, 10)
        # screen.blit(text_surf,text_rect)
        score = display_score()
        
        # moving sprite 
        # snail_rect.x -= 6
        # if snail_rect.right <= 0: 
        #     snail_rect.left = 800 

        # gravity
        player_gravity += 1
        player_rect.y += player_gravity
        
        # keep player on ground
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
            player_gravity = 0
        
        # sprites
        # screen.blit(snail_surf, snail_rect)
        screen.blit(player_surf, player_rect)
    
    # Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
    
    # collision / quit
        for obstacle_rect in obstacle_rect_list:
            if player_rect.colliderect(obstacle_rect):
                game_state = False
                break
            
    # animation
        player_animation()
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_name, game_name_rect)
        score_message = font.render(f'Your score: {score}',False,(111,196,169))
        score_message_rect = score_message.get_rect(center = (400,330))
        
        if score == 0:
            screen.blit(game_message,game_message_rect)
        else: 
            screen.blit(score_message,score_message_rect)
# scaling
    
    pg.display.update()
    clock.tick(60)
