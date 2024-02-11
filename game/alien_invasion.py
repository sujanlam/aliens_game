import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    """Start the game and create a screen"""
    pygame.init()
    """Initialize pygame, settings and screen object"""
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_width))
    pygame.display.set_caption("Alien Invasion")
    print('Set display')

    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group tp store bullets in.
    bullets = Group()
    """Start the loop in the game"""
    while True:
        """Keyboard and mouse events"""
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # Get rid of bullets that disappear
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
