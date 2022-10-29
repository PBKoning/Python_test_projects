# How to run Pygame fullscreen on a Chromebook
# Width and height need to match screen resolutiob to prevent an error

import pygame

pygame.display.init()

width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
window_surface = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

running = True
clock = pygame.time.Clock()


while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    pygame.display.update()