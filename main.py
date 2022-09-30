import pygame
import random
import os
from pygame import mixer


# Initialise pygame
mixer.init()
pygame.init()

"""
    CONSTANTS
"""
# game window dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# frame rate
FPS = 60

# Colours 
WHITE = (255,255, 255)
BLACK = (0, 0, 0)
PANEL = (153, 217, 234)

# create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('HHH')

"""
    VARIABLES
"""
# set frame rate 
clock = pygame.time.Clock()


# load music and sounds

# load images
bg_image = pygame.image.load('assets/bg.png').convert_alpha()
# game variables

"""
    GAME
"""
run = True
while run:
    clock.tick(FPS)
    # draw background
    screen.blit(bg_image, (0,0))
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # update display window
    pygame.display.update()
    
pygame.quit()
