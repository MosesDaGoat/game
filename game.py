import pygame
import sys
from scripts.util import load_image, load_images
from scripts.gameconfig import GameConfig

class Game:
    def __init__(self):
        
        pygame.init()
        
        pygame.display.set_caption("flappy bird")
        
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((700, 900))
        self.display = pygame.Surface((551, 720))
                
        clock = pygame.time.Clock()
        
        self.movement = [False, False]

        self.assets = {
            'background': load_image('background/background.png'),
            "bird": load_images('birdsprites'),
            "pipe": load_images('pipes'),
            "gameover": load_image('gameover/gameover.png'),
            "floor": load_image('floor/ground.png')
        }

        self.config = GameConfig(self.display.get_width(), self.display.get_height(), self.assets['floor'])

    def run(self):
        while True:
            self.display.blit(self.assets['background'], (0, 0))

            self.config.update_ground()
            self.config.draw_ground(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            

            self.screen.blit(pygame.transform.scale(self.display,self.screen.get_size()),(0,0)),
            pygame.display.update()
            self.clock.tick(60)

Game().run()