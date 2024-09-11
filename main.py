import pygame
from sys import exit 



class Game:
    def __init__(self):
        self.movement = [False, False]
        self.player = Player(self)
        
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        self.display = pygame.Surface((600, 400))
        
        pygame.display.set_caption("flappy bird")
        
        clock = pygame.time.Clock()


def run_game(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.movement[0] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.movement[0] = False

        self.screen.blit(pygame.transform.scale(self.display,self.screen.get_size())),
        pygame.display.update()
        self.clock.tick(60)