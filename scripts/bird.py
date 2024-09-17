import pygame

class Bird:
    def __init__(self, animation, x, y):
        self.animation = animation
        self.x = x
        self.y = y

    def update(self):
        self.animation.update()

    def draw(self, surface):
        surface.blit(self.animation.img(), (self.x, self.y))