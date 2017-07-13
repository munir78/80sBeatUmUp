import pygame
import os

WIDTH = 800
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#asset folder
game_folder = os.path.dirname(__file__) #the folder in which this file is in
img_folder = os.path.join(game_folder, "img") # location of img assets

class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        # this line is required to properly create the sprite
        pygame.sprite.Sprite.__init__(self)
        # create a plain rectangle for the sprite image  self.image = pygame.Surface((50, 50))

        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        self#.image.fill(BLUE)
        self.image.set_colorkey(BLACK) # makes this colour transparent
        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
        # center the sprite on the screen
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        # any code here will happen every time the game loop updates
        self.rect.x += 5 # the rectangle goes to the side
        if self.rect.left > WIDTH: # if the left side of the rectangle is larger than width then it goes all the way to the beginning, right side becomes 0
            self.rect.right = 0

# initialize pygame and create window
pygame.init()
pygame.mixer.init() #gives audio functionality
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()