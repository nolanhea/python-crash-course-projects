import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set it's starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get it's rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

    def update(self):
        if self.moving_right and self.rect.bottomright[0] <= self.screen_rect.bottomright[0]:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.x >= 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
    def blitme(self):
        # Start each new ship at the bottom center of the screen
        self.screen.blit(self.image, self.rect)