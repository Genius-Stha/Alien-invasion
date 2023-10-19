import pygame.font

class Button():
    def __init__(self,ai_settings,screen,msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        #set dimensions of the buttons
        self.width,self.height = 200,50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)
        
        #build the button's rect object and center it
        self.rect= pygame.Rect(0,0,self.width,self.height)
        self.rect.center =self.screen_rect.center
        
        #prepare the button message
        self.prep_msg(msg)
        self.show_controls()
    
    def prep_msg(self,msg):
        '''Turn msg into rendered image and center it'''
        self.msg_image =self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect= self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
    
    def show_controls(self):
        self.show_message = 'Controls are'
        self.show_controls = '<- "left" -> "right" "q" -> quit  [SPACE] -> "SHOOT"'
        self.show_text = f'{self.show_message} {self.show_controls}'  # Combine the two strings
        self.show_image = self.font.render(self.show_text, True, self.text_color, (30, 30, 30))
        self.show_image_rect = self.show_image.get_rect()
        self.show_image_rect.topleft = (10, 10)  # Set the top-left corner position

    def draw_button(self):
        #draw blank button and then draw message
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
        #self.screen.blit(self.show_image,self.show_image_rect)
        
        #remove # to show controls
    