import pygame as pg
from sys import exit    

pg.init()
screen = pg.display.set_mode((800, 400), pg.RESIZABLE)
pg.display.set_caption("Image Display")
clock = pg.time.Clock()
link = "D:\Pygame\Jia Jie\InputFiles\Font\Pixeltype.ttf"
font = pg.font.Font(link,50)
# pg.font.Font(font style, font size)   <font>

sky_surface = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\Sky.png").convert_alpha()
ground_surface = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\ground.png").convert_alpha()
# this is how you import images. Convert alpha makes the pictures easier to handle in the future when editing
text_surface = font.render("Hello", True, "Black")
# font.render(<text>, <anti-aliasing>, <color>)
snail_surface = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\snail\snail1.png").convert_alpha()
snail_x_pos = 600
player_surface = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\player\player_walk_1.png").convert_alpha()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    # screen.blit(obj, (coordinates))
    screen.blit(sky_surface,(0, 0))
    screen.blit(ground_surface,(0, 300))
    screen.blit(text_surface,(350, 50))
    snail_x_pos -= 2
    screen.blit(snail_surface, (snail_x_pos,250))
    if snail_x_pos < -100: 
        snail_x_pos = 800
    screen.blit(player_surface, (80, 200))
    pg.display.update()
    clock.tick(120)
