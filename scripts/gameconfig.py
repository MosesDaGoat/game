import pygame

class GameConfig:
    def __init__(self, screen_width, screen_height, floor_image):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.floor_image = floor_image
        self.scroll_speed = 4
        self.floor_y = screen_height - floor_image.get_height()
        self.ground_objects = [self.create_ground(0)]

    def create_ground(self, x):
        return {
            'x': x,
            'y': self.floor_y,
            'image': self.floor_image
        }

    def update_ground(self):
        # Remove off-screen ground objects
        self.ground_objects = [ground for ground in self.ground_objects if ground['x'] > -self.floor_image.get_width()]

        # Add new ground objects if needed
        if len(self.ground_objects) <= 2:
            last_x = self.ground_objects[-1]['x'] + self.floor_image.get_width() if self.ground_objects else 0
            new_ground = self.create_ground(last_x)
            self.ground_objects.append(new_ground)

        # Update ground positions
        for ground in self.ground_objects:
            ground['x'] -= self.scroll_speed

    def draw_ground(self, surface):
        for ground in self.ground_objects:
            surface.blit(ground['image'], (ground['x'], ground['y']))