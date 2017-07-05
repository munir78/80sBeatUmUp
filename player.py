import pygame
class Player:

    hearts = 0
    x = 200
    y = 300
    dx = 0
    dy = 0

    def __init__(self, hearts):
        self.hearts = hearts

    def update(self, screen):
        self.x += self.dx
        self.y += self.dy
        self.dx = self.dx * 0.8
        self.dy = self.dy * 0.8
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 100, 100))

    def move(self, dx,dy):
        self.dx = dx
        self.dy = dy