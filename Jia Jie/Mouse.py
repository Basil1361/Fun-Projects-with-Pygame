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
text_surf = font.render("Hello", True, "Black")
text_rect = text_surf.get_rect(center = (400, 50))

# snail
snail_surf = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\snail\snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

# player
player_surf = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\player\player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(bottomright = (80, 300))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        # if event.type == pg.MOUSEMOTION:
        #     print(event.pos)
        # checking coordinates
        
        # if event.type == pg.MOUSEBUTTONDOWN:
        #     print('Mouse Down')
        # # triggered in pressed
        
        # if event.type == pg.MOUSEBUTTONUP:
        #     print('Mouse Up')
        # triggered if released after pressed
        

    screen.blit(sky_surf,(0, 0))
    screen.blit(ground_surf,(0, 300))
    screen.blit(text_surf,text_rect)
    snail_rect.x -= 4
    if snail_rect.right <= 0: 
        snail_rect.left = 800 

    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)
    
    # mouse collision
    # mouse_point = pg.mouse.get_pos()
    # if player_rect.collidepoint(mouse_point):
    #     print(pg.mouse.get_pressed())
        

    pg.display.update()
    clock.tick(120)
