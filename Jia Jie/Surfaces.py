import pygame as pg
from sys import exit    

pg.init()
screen = pg.display.set_mode((800, 800), pg.RESIZABLE)
pg.display.set_caption("Image Display")
clock = pg.time.Clock()

test_surface = pg.Surface((100,100))
test_surface.fill('blue')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    screen.blit(test_surface, (200,100))
    # original point is at top left 
    # blit = block image transfer
    # The blit method is used to draw the surface onto the screen at the specified position.

    pg.display.update()
    clock.tick(60)
