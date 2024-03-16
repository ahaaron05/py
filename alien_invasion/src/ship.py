import pygame

class Ship:
    """manage the ship"""

    def __init__(self, game):
        """Initialize the ship object and set starting position"""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Load ship image and get its rect
        self.image = pygame.image.load("alien_invasion/space_ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.x = float(self.rect.x)
        # Movement flag
        self.moving_right= False
        self.moving_left = False
    
    def update(self):
        """Update ship position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.move_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.move_speed
        
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its curent location"""
        self.screen.blit(self.image, self.rect)