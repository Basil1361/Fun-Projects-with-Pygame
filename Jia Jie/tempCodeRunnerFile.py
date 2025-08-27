'''
player_stand = pg.image.load("D:\Pygame\Jia Jie\InputFiles\graphics\Player\player_stand.png").convert_alpha()
player_stand_scale = pg.transform.scale(player_stand, (200,200))
player_stand_rect = player_stand_scale.get_rect(center = (400,200))
...
screen.blit(player_stand_scale, player_stand_rect)
'''