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
text_surf = font.render("Hello", True, color)
text_rect = text_surf.get_rect(center = (400, 50))

# snail
snail_surf = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\snail\snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

# player
player_surf = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\player\player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(bottomright = (80, 300))

colorhex = "#c0ec8d"
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
            
    screen.blit(sky_surf,(0, 0))
    screen.blit(ground_surf,(0, 300))
    pg.draw.rect(screen, colorhex ,text_rect)
    pg.draw.rect(screen, colorhex ,text_rect, 10)
    # pg.draw.line(screen, "Pink", (0,0), pg.mouse.get_pos(), 10)
    screen.blit(text_surf,text_rect)
    snail_rect.x -= 4
    if snail_rect.right <= 0: 
        snail_rect.left = 800 

    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)
    

    pg.display.update()
    clock.tick(120)
