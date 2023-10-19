import pygame


class Ship:
    def __init__(self,screen,ai_settings):
        self.screen = screen
        
        self.ai_settings=ai_settings
        
        
        #load the ship image
        self.spaceship=pygame.image.load('images/ship.png')
        
        #spaceship is huge so transforming it 
        self.game_spaceship=pygame.transform.scale(self.spaceship,(55,40))
        #rect for storing the ship coordinates
        self.rect =self.game_spaceship.get_rect()
        
        #taking the screen coordinates for position of the ship
        self.screen_rect=screen.get_rect()
        #getrect gives x and y position and the width and height of the ship
        
        #start each shop at the bottom center of the screen.
        #since rect holds the ship coordinates centerx holds x coordinates
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        
        
        #making float for smooth movement of spaceship
        self.center=float(self.rect.centerx)
        
        #movement flag
        self.moving_right=False
        self.moving_left=False

    def update(self):
        '''update the shape position based on the movement flag'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor         # speed factor
            
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #update rect object form self.center
        self.rect.centerx=self.center
    def center_ship(self):
        self.center =self.screen_rect.centerx
    def blitme(self):
        '''draw space ship at it's location.'''
        self.screen.blit(self.game_spaceship,self.rect)
