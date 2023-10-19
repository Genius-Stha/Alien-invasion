import pygame
from pygame.sprite  import Sprite

class Alien(Sprite):
    
    def __init__(self,ai_settings,screen):
        '''Initialize the alien and set its starting position'''
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #load the alien image and set its rect attributes
        self.image = pygame.image.load('images/enemy.png')
        self.alien_spaceship= pygame.transform.scale(self.image,(55,40))
        self.rect=self.alien_spaceship.get_rect()
        
        #start each new alien near the top of the screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        
        #store the alien position
        self.x=float(self.rect.x)
        
    def update(self):
        '''move the alien'''
        self.x += (self.ai_settings.alien_speed_factor* self.ai_settings.fleet_direction)
        self.rect.x = self.x
        
    def check_edges(self):
        '''return True if alien is on the edge of the screen'''
        screen_rect =self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    def blitme(self):
        '''draw the alien in current position'''
        self.screen.blit(self.alien_spaceship,self.rect)        

