# PaddleGame - A simple paddlegame made with PyGame

import pygame

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
SURFACE_COLOR = (0, 0, 0)
RED = RED = (255, 0, 0)
PADDLE_SPEED = 5

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
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
  
        self.rect = self.image.get_rect()
        self.rect.x = int((SCREEN_WIDTH - self.width) / 2) # position sprite in middle of screen
        self.rect.y = SCREEN_HEIGHT - self.height - 5 # position sprite just above the bottom of the screen
    
    # function to move to the right
    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > (SCREEN_WIDTH - self.width):
            self.rect.x = SCREEN_WIDTH - self.width
 
    # function to move to the left
    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0
    

# Create sprites and add to sprite list
all_sprites_list = pygame.sprite.Group()
player_paddle = Paddle(RED, 50, 10)
all_sprites_list.add(player_paddle)

# Gameloop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle input of keys
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]: # move left
        player_paddle.moveLeft(PADDLE_SPEED)
    if keys[pygame.K_RIGHT]: # move right
        player_paddle.moveRight(PADDLE_SPEED)
    if keys[pygame.K_q]: # quit game   
        running = False

    # Draw game
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    fps_clock.tick(60)
  
pygame.quit()