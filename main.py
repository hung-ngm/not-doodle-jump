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

# Platform constant
MAX_PLATFORMS = 10
PLATFORM_HEIGHT = 10
PLATFORM_MIN_WIDTH = 40
PLATFORM_MAX_WIDTH = 70
PLATFORM_MIN_HEIGHT_DIFF = 80
PLATFORM_MAX_HEIGHT_DIFF = 120

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
platform_image = pygame.image.load('assets/wood.png').convert_alpha()

"""
    PLATFORM
"""
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_image, (width, PLATFORM_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# game variables

# Create platform group
platform_group = pygame.sprite.Group()

# Create temporary platforms
for p in range(MAX_PLATFORMS):
    p_w = random.randint(PLATFORM_MIN_WIDTH, PLATFORM_MAX_WIDTH)
    p_x = random.randint(0, SCREEN_WIDTH - p_w)
    p_y = p * random.randint(PLATFORM_MIN_HEIGHT_DIFF, PLATFORM_MAX_HEIGHT_DIFF)
    new_platform = Platform(p_x, p_y, p_w)
    platform_group.add(new_platform)

"""
    GAME
"""
run = True
while run:

    clock.tick(FPS)

    # draw background
    screen.blit(bg_image, (0,0))

    # draw sprites
    platform_group.draw(screen)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # update display window
    pygame.display.update()
    
pygame.quit()
