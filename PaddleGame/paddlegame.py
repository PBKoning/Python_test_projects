# PaddleGame - A simple paddlegame made with PyGame

import pygame

# Constants
SCREEN_WIDTH = 640
SCREEN_HIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HIGHT)
SURFACE_COLOR = (0, 0, 0)
RED = RED = (255, 0, 0)

# Setup game
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Paddle Game")

# Global variables
running = True
fps_clock = pygame.time.Clock()

# Object paddle
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
  
        self.image = pygame.Surface([width, height])
        # self.image.fill(SURFACE_COLOR)
        # self.image.set_colorkey(COLOR)
  
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
  
        self.rect = self.image.get_rect()

# Create sprites and add to sprite list
all_sprites_list = pygame.sprite.Group()
player_paddle = Paddle(RED, 50, 10)
all_sprites_list.add(player_paddle)

# Gameloop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw game
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    fps_clock.tick(60)
  
pygame.quit()