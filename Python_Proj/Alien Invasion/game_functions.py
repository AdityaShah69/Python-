import sys
import pygame
from bullet import Bullet
from ship import Ship
from alien import Alien
from pygame.sprite import Sprite

def check_events(ship,ai_settings,screen,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings,screen,ship,bullets,alien,aliens):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    alien.blitme()
    pygame.display.flip()

def update_ship(ship):
    ship.update()

def update_bullets(bullets):
       bullets.update()

def update_aliens(ai_settings,aliens):
    """ Chaeck if the fleet is at an edge, and then update the postions of all aliens in the fleet."""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x

def get_number_row(ai_settings,alien_height,ship_height):
    available_space_y =ai_settings.screen_height -( 3* alien_height) - ship_height
    number_row = int(available_space_y/(2*alien_height))
    return number_row


def create_fleet(ai_settings,screen,aliens):
    """Create a full fleet of aliens """
    # Create an alien and find the number of aliens in a row
    # Spacing between each alien is ewual to one alien width

    alien = Alien(ai_settings,screen)
    ship = Ship(screen,ai_settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    ship_height = ship.rect.height
    number_aliens_x =get_number_aliens_x(ai_settings,alien_width)
    number_row = get_number_row(ai_settings,alien_height,ship_height)
    # Create the first row of aliens 
    for row_number in range(number_row):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 *alien_width*alien_number
    alien.rect.y = alien.rect.height + 2*alien.rect.height *row_number
    alien.rect.x = alien.x
    aliens.add(alien)


def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

