import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''A class to manage the bullets fired from the ship'''
    def __init__(self,ai_settings ,screen, ship) -> None:
        super(Bullet,self).__init__()
        self.screen = screen
        
        #create a bullet rect at 0,0 and then set correct position.
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #store bullet position and float
        self.y = float(ship.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        ''' move bullet position'''
        self.y -= self.speed_factor
        
        #update rect position
        self.rect.y =self.y
        
    def draw_bullet(self):
        ''' draw bullet on screen'''
        pygame.draw.rect(self.screen, self.color,self.rect)
        