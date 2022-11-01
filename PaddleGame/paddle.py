import pygame

# Game contants
from constants import *

# Object paddle
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
  
        self.rect = self.image.get_rect()
        self.rect.x = int((SCREEN_WIDTH - self.width) / 2) # position sprite in middle of screen
        self.rect.y = SCREEN_HEIGHT - self.height - 5 # position sprite just above the bottom of the screen
    
    def update(self):
        
        # Position paddle according to mouse position
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = mouse_pos[0]
        if self.rect.x > (SCREEN_WIDTH - self.width):
            self.rect.x = SCREEN_WIDTH - self.width