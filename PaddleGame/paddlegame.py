# PaddleGame - A simple paddlegame made with PyGame

import pygame

# Paddle object
from paddle import Paddle
from ball import Ball

# Constants
from constants import *

# Global variables to run PyGame
running = True
fps_clock = pygame.time.Clock()

# Setup game
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Paddle Game")
pygame.mouse.set_visible(False) # Hide mouse cursor

# Create sprites and add to sprite list
all_sprites_list = pygame.sprite.Group()
player_paddle = Paddle(RED, 50, 10)
all_sprites_list.add(player_paddle)
ball = Ball(RED, 10, 10, 50, 50, 0.75, 1.25)
all_sprites_list.add(ball)

# Gameloop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle input of keys
    keys = pygame.key.get_pressed() 
    # if keys[pygame.K_LEFT]: # move left
    #     player_paddle.moveLeft(PADDLE_SPEED)
    # if keys[pygame.K_RIGHT]: # move right
    #     player_paddle.moveRight(PADDLE_SPEED)
    
    if keys[pygame.K_q]: # quit game   
        running = False

    # Draw game
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    fps_clock.tick(60)
  
pygame.quit()