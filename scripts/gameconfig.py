import pygame

class GameConfig:
    def __init__(self, screen_width, screen_height, floor_image):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.floor_image = floor_image
        self.scroll_speed = 4
        self.floor_y = screen_height - floor_image.height
        self.ground_width = floor_image.width
        self.ground_x = 0

    def update_ground(self):
        self.ground_x -= self.scroll_speed
        if self.ground_x <= -self.ground_width:
            self.ground_x = 0

    def draw_ground(self, surface):
        first_tile_x = self.ground_x
        while first_tile_x < self.screen_width:
            surface.blit(self.floor_image, (first_tile_x, self.floor_y))
            first_tile_x += self.ground_width