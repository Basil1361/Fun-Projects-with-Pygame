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
snail_rect = snail_surface.get_rect(bottomright = (600, 300))

player_surface = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\player\player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(bottomright = (80, 300))

# rect_surface = pg.Rect(left,top,width,height)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    # screen.blit(obj, (coordinates))
    screen.blit(sky_surface,(0, 0))
    screen.blit(ground_surface,(0, 300))
    screen.blit(text_surface,(300, 50))
    snail_rect.x -= 4
    if snail_rect.right <= 0: 
        snail_rect.left = 800 
# 800 is the width of the screen
    screen.blit(snail_surface, snail_rect)
    # if you want to print something print(player_rect.left)
    screen.blit(player_surface, player_rect)
    pg.display.update()
    clock.tick(120)
