import pygame

# Game contants
from constants import *

# Object ball
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y, x_speed, y_speed):
        super().__init__()
        self.width = width
        self.height = height
        self.x = x # x-position where speed is added, can also be a float
        self.y = y # same for y position
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.image = pygame.Surface([width, height])
        
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
  
        self.rect = self.image.get_rect()
        self.rect.x = self.x # position ball
        self.rect.y = self.y
    
    def update(self):
        # change x and y by speed
        self.x += self.x_speed
        self.y += self.y_speed
        # convert to int and adjust the x and y of the sprite
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        
        