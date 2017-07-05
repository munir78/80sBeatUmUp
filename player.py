import pygame
class Player:

    hearts = 0
    x = 0
    y = 0

    def __init__(self, hearts):
        self.x = 200
        self.y = 300
        self.hearts = hearts

    def update(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 100, 100))

    def move(self, dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy

