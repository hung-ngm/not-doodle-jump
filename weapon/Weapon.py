import pygame
import random

class Weapon(pygame.sprite.Sprite):
    def __init__(self, SCREEN_HEIGHT, x, y, sprite_sheet, scale):
        
        pygame.sprite.Sprite.__init__(self)
        # movement
        # self.direction = 1 #random.choice([-1, 1])
        # self.flip = False #True if self.direction == -1 else False
        
        # animation
        self.animation_list = []
        self.frame_index = 0
        self.last_update_time = pygame.time.get_ticks()
        self.ANIMATIONS = 1
        
        # load image animation
        for animation_index in range(1, self.ANIMATIONS + 1):
            image = sprite_sheet.get_image(animation_index, 64, 64, scale, (0, 0, 0))
            image = pygame.transform.flip(image, flip_x = True, flip_y = False)
            image.set_colorkey((0, 0, 0))
            self.animation_list.append(image)
        
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self, scroll = 0, SCREEN_HEIGHT = 600, shuriken_speed = 7):
        ANIMATION_COOLDOWN = 1000/60 #ms
        
        self.image = self.animation_list[self.frame_index]
        if (pygame.time.get_ticks() - self.last_update_time) > ANIMATION_COOLDOWN:
            self.last_update_time = pygame.time.get_ticks()
            self.frame_index = (self.frame_index + 1) % self.ANIMATIONS
        
        # move object
        # self.rect.x += self.direction * 2
        self.rect.y += scroll - shuriken_speed

        # isOffScreen
        if self.rect.bottom < 0:
            self.kill()