import pygame.font

class GameStats():
    def __init__(self,ai_settings):
        
        self.ai_settings = ai_settings
        self.reset_stats()
        
        #set alien invasion in an active state
        self.game_active = False
    def reset_stats(self):
        self.score=0
        self.level=1
        self.ships_left = self.ai_settings.ship_limit
        
class Scoreboard():
    def __init__(self,ai_settings,screen,stats):
        self.screen = screen
        self.screen_rect =screen.get_rect()
        self.ai_settings =ai_settings
        self.stats=stats
        
        #font settings
        self.text_color = (30,30,30)
        self.font =pygame.font.SysFont(None,48)
        
        #prepare the initial score image
        self.prep_score()
        self.prep_level()
        
        
    def prep_score(self):
        '''Turn the score into a rendered image'''
        score_str='Score:'+str(self.stats.score)        
        self.score_image = self.font.render(score_str,True, self.text_color,self.ai_settings.bg_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right =self.screen_rect.right -20
        self.score_rect.top=20
        

        
    def prep_level(self):
        self.display_level= 'LEVEL : ' + str(self.stats.level)
        self.level_image =self.font.render(self.display_level,True,self.text_color,self.ai_settings.bg_color)
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.score_rect.right
        self.level_rect.top =self.score_rect.bottom +10
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.level_image,self.level_rect)

        