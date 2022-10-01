import pygame
import random

from constant import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, moving, platform_image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_image, (width, PLATFORM_HEIGHT))
        self.moving = moving
        self.move_counter = random.randint(0, 50)
        self.direction = random.choice([-1, 1])
        self.speed = random.randint(1, 2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self, scroll):
        # Moving platform side to side
        if self.moving == True:
            self.move_counter += 1
            self.rect.x += self.direction * self.speed
        
        if self.move_counter >= 100 or self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.direction *= -1
            self.move_counter = 0
        
        # Update platform's vertical position
        self.rect.y += scroll

        # Check if platform has gone off screen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()