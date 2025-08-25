import pygame as pg
from sys import exit    

pg.init()
screen = pg.display.set_mode((800, 400), pg.RESIZABLE)
pg.display.set_caption("Image Display")
clock = pg.time.Clock()
link = "D:\Pygame\Jia Jie\InputFiles\Font\Pixeltype.ttf"
font = pg.font.Font(link,50)
# pg.font.Font(font style, font size)   <font>

sky_surface = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\Sky.png")
ground_surface = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\ground.png")
# this is how you import images. 
text_surface = font.render("Hello", True, "Black")
# font.render(<text>, <anti-aliasing>, <color>)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    # screen.blit(obj, (coordinates))
    screen.blit(sky_surface,(0, 0))
    screen.blit(ground_surface,(0, 300))
    screen.blit(text_surface,(350, 50))
    
    pg.display.update()
    clock.tick(60)
