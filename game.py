import pygame
from sys import exit 



class Game:
    def __init__(self):
        
        pygame.init()
        
        pygame.display.set_caption("flappy bird")
       
        self.screen = pygame.display.set_mode((1200, 800))
        self.display = pygame.Surface((600, 400))
        
        
        
        clock = pygame.time.Clock()
        
        self.movement = [False, False]

def run_game(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
         

        self.screen.blit(pygame.transform.scale(self.display,self.screen.get_size()),(0,0)),
        pygame.display.update()
        self.clock.tick(60)