import pygame

WIDTH = 1280
HEIGHT = 720

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

x_val = 150
y_val = 200
# Game loop
done = False
while not done:
    ## Inputs go here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         done = True
## Game logic goes in here
    screen.fill(BLACK)

## Draw here
    pygame.draw.rect(screen, WHITE, (x_val, y_val, 20, 20))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()