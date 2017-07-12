import pygame
class Player:

    x = 200
    y = 300
    dx = 0
    dy = 0
    falling = False


    def update(self, screen):
        self.x += self.dx
        self.dx *= 0.9



        print(self.dy)
        self.y += self.dy
        self.dx = self.dx * 0.8
        self.dy = self.dy * 0.8
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 100, 100))

    def move(self, dx):
        self.dx += dx

    def jump(self, dy):
        self.dy += dy
