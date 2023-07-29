import sys
import pygame
import time
from settings import Settings
from ship import Ship
from bullet import Bullet
class AlienInvasion:
    """Class to manage game assets and behaviour"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop fo the game"""
        while True:
            time.sleep(0.005)
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()


    def _check_events(self):
        # Watch the keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        # Make most recently drawn screen visible:
        pygame.display.flip()



if __name__ == '__main__':
    # Make a game instance and run a game.
    ai = AlienInvasion()
    ai.run_game()