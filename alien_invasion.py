import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from scoreboard import Scoreboard
import game_function as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(screen,"Play")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    ship = Ship(ai_settings,screen)
    aliens = Group()
    bullets = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    '''gf.create_random(aliens,screen,aliens)'''


    while True:
        gf.check_events(ai_settings,screen,ship,aliens,bullets,stats,play_button)

        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_settings, screen, ship, aliens, stats, bullets)
            gf.update_bullets(ai_settings,stats,screen,ship,aliens,bullets,sb)

        gf.update_screen(ai_settings,screen,ship,aliens,bullets,stats,play_button,sb)


run_game()