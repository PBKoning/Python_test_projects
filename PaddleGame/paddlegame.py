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
paddle = Paddle(color=RED, width=50, height=10)
all_sprites_list.add(paddle)
ball = Ball(color=RED, width=10, height=10, x=50, y=50, x_speed=2.75, y_speed=3.5)
all_sprites_list.add(ball)

# Init sound effects
snd_ball_hit = pygame.mixer.Sound(r'./PaddleGame/ball_hit.wav')


# Gameloop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle input of keys
    keys = pygame.key.get_pressed()         
    if keys[pygame.K_q]: # quit game   
        running = False             

    # Check if ball hits paddle
    if ball.y_speed > 0 and pygame.Rect.colliderect(paddle.rect, ball.rect):
        ball.y_speed *= -1
        snd_ball_hit.play()
    # Check if ball hits left or right 'wall'
    if ball.x < 0 or  ball.x > SCREEN_WIDTH - ball.width:
        ball.x_speed *= -1
        snd_ball_hit.play()
    # Check if ball hits top
    if ball.y < 0:
        ball.y_speed *= -1
        snd_ball_hit.play()


    # Draw game
    all_sprites_list.update()
    screen.fill(SURFACE_COLOR)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    fps_clock.tick(60)
  
pygame.quit()