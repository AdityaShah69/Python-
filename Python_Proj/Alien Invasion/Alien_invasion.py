import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from bullet import Bullet
from alien import Alien


def run_game():
    # initialize pygame
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen, ai_settings)
    alien = Alien(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens)
    while True:
        gf.check_events(ship, ai_settings, screen, bullets)
        gf.update_ship(ship)
        gf.update_bullets(bullets)

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        
        gf.update_aliens(aliens, ai_settings)
        # aliens.update()
        # gf.check_fleet_edges(aliens,ai_settings)
        gf.update_screen(ai_settings, screen, ship, bullets, alien, aliens)


run_game()
