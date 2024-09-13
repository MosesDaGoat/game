import pygame
import sys
from scripts.util import load_image, load_images
from scripts.gameconfig import GameConfig

class Game:
    SCREEN_SIZE = (700, 900)
    DISPLAY_SIZE = (551, 720)
    FPS = 60

    def __init__(self):
        pygame.init()
        self._setup_display()
        self._load_assets()
        self._setup_game_objects()

    def _setup_display(self):
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        self.display = pygame.Surface(self.DISPLAY_SIZE)

    def _load_assets(self):
        self.assets = {
            'background': load_image('background/background.png'),
            "bird": load_images('birdsprites'),
            "pipe": load_images('pipes'),
            "gameover": load_image('gameover/gameover.png'),
            "floor": load_image('floor/ground.png')
        }

    def _setup_game_objects(self):
        self.config = GameConfig(self.DISPLAY_SIZE[0], self.DISPLAY_SIZE[1], self.assets['floor'])

    def run(self):
        while True:
            self._handle_events()
            self._update()
            self._draw()
            self._update_display()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit()

    def _update(self):
        self.config.update_ground()

    def _draw(self):
        self.display.blit(self.assets['background'], (0, 0))
        self.config.draw_ground(self.display)

    def _update_display(self):
        scaled_display = pygame.transform.scale(self.display, self.SCREEN_SIZE)
        self.screen.blit(scaled_display, (0, 0))
        pygame.display.update()
        self.clock.tick(self.FPS)

    def _quit(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Game().run()