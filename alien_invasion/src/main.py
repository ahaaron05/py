import sys
import pygame
from settings import Settings
from ship import Ship

class Game:
    """Manages game and behavior"""

    def __init__(self):
        """Initialize and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
    
    def runGame(self):
        """Start the main loop for the game"""
        while (True):
            self.check_events()
            self.ship.update()
            self.update_screen()
    
    def check_events(self):
        """Respond to keyboard and mouse input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def update_screen(self):
        """Updates main game loop and flips"""
        self.screen.fill(self.settings.screen_color)
        self.ship.blitme()

        pygame.display.flip()
    

if (__name__ == '__main__'):
    game = Game()
    game.runGame()