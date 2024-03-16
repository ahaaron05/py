import pygame

class Settings:
    """Store all settings for the game"""

    def __init__(self):
        """Initialize games settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (0, 0, 0)
        
        # Movement 
        self.move_speed = 0.8
        
        # Other 
        self.icon = pygame.image.load("alien_invasion/space_ship.bmp")
        pygame.display.set_icon(self.icon)