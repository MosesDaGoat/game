from scripts.animation import Animation
from scripts.physics import Physics
import pygame

class Bird(Physics):
    def __init__(self, animation, x, y):
        super().__init__()
        self.animation = animation
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, animation.img().get_width(), animation.img().get_height())
        self.flap = False

    def update(self):
        if not self.flap:
            self.gravity()
        self.animation.update()
        self.rect.y += int(self.vel)
        if self.rect.y < 0:
            self.rect.y = 0

    def draw(self, surface):
        surface.blit(self.animation.img(), self.rect)