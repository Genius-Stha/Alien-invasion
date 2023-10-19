class Settings():
    def __init__(self) -> None:
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(0,0,0)
        
        #ship speed setting
        self.ship_speed_factor=2
        self.ship_limit=3
        
        #bullet speed setting
        self.bullet_speed_factor=3
        self.bullet_width= 3
        
        self.bullet_height=15
        self.bullet_color=(250,0,0)
        self.bullet_allowed = 10
        
        #alien speed setting
        self.alien_speed_factor=2
        self.fleet_drop_speed =10
        
        #fleet direction 1 is for right and -1 for left
        self.fleet_direction =1
        
        #how quickly the game speeds up
        self.speedup_factor = 1.3
        
        #how quickly the alien point increases
        self.score_scale=1.5
        
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        '''Initialize setings that chang through the game'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction=1

        #scoring
        self.alien_points =50
        
    def increase_speed(self):
        '''Increment speed'''
        self.ship_speed_factor *= self.speedup_factor
        self.bullet_speed_factor *= self.speedup_factor
        self.alien_speed_factor *= self.speedup_factor
        
        self.alien_points = int(self.alien_points *self.score_scale)
        
        #check alien points now
        print(self.alien_points)