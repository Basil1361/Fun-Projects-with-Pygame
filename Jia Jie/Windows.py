import sys, pygame

pygame.init()
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Window")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:          # window X button
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False                    # ESC to quit

    screen.fill((30, 30, 30))                  # dark gray background
    pygame.display.flip()                      # swap buffers
    clock.tick(60)                             # limit to 60 FPS

pygame.quit()
sys.exit()
