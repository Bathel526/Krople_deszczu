import pygame
from pygame.sprite import Sprite

class Krople(Sprite):
    def __init__(self, ai_animation):
        super().__init__()
        self.screen = ai_animation.screen
        self.image = pygame.image.load('pictures/kropla50.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.y = self.rect.width
        self.rect.x = self.rect.height
        
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def check_bottom_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            return True
        else:
            return False
        
    def update(self):
        self.y += 1.0
        self.rect.y = self.y
