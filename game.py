import pygame
import sys
from scripts.util import load_image, load_images


class Game:
    def __init__(self):
        
        pygame.init()
        
        pygame.display.set_caption("flappy bird")
        
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((500, 800))
        self.display = pygame.Surface((643, 900))
                
        clock = pygame.time.Clock()
        
        self.movement = [False, False]

        self.assets = {
            'background': load_image('background/background.png'),
        }


    def run(self):
        
        while True:
            self.display.blit(self.assets['background'], (0, 0))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            

            self.screen.blit(pygame.transform.scale(self.display,self.screen.get_size()),(0,0)),
            pygame.display.update()
            self.clock.tick(60)

Game().run()