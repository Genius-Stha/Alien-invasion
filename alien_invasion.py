import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats ,Scoreboard
from pygame.sprite import Group
from buttons import Button


pygame.init()
ai_settings=Settings()          #setting game defaults

screen = pygame.display.set_mode(      #setting game screen
    (ai_settings.screen_width,ai_settings.screen_height)
)
pygame.display.set_caption("Alien Invasion")

#make a ship , group of bullets and aliens
ship=Ship(screen,ai_settings)

bullets = Group()

aliens = Group()

#create a fleet of alien objects
gf.create_fleet(ai_settings,screen,ship,aliens)

#make a play button.
play_button = Button(ai_settings,screen,'Play')
#create a instance to store the game statistics
stats = GameStats(ai_settings)
sb = Scoreboard(ai_settings,screen,stats)
#Start
def run_game():
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(aliens,bullets,ai_settings,stats,sb)
            gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)


run_game()




