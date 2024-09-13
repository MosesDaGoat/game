import pygame

class GameConfig:
    def __init__(self, screen_width, screen_height, floor_image):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.floor_image = floor_image
        self.scroll_speed = 4
        self.floor_y = screen_height - floor_image.get_height()
        self.ground_width = floor_image.get_width()
        self.ground_objects = [self._create_ground(0)]

    def _create_ground(self, x):
        return {'x': x, 'y': self.floor_y}

    def _get_last_ground_x(self):
        return self.ground_objects[-1]['x'] if self.ground_objects else 0

    def update_ground(self):
        # Remove off-screen ground objects
        self.ground_objects = [ground for ground in self.ground_objects if ground['x'] > -self.ground_width]

        # Add new ground objects if needed
        while len(self.ground_objects) < 3:  # Ensure we always have at least 3 ground objects
            new_x = self._get_last_ground_x() + self.ground_width
            self.ground_objects.append(self._create_ground(new_x))

        # Update ground positions
        for ground in self.ground_objects:
            ground['x'] -= self.scroll_speed

    def draw_ground(self, surface):
        for ground in self.ground_objects:
            surface.blit(self.floor_image, (ground['x'], ground['y']))