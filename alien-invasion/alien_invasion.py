import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Class to manage game assets and behaviour"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop fo the game"""
        while True:
            # Watch the keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            # Make most recently drawn screen visible:
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run a game.
    ai = AlienInvasion()
    ai.run_game()