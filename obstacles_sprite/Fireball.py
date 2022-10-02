import pygame
import random

class Fireball(pygame.sprite.Sprite):
    def __init__(self, SCREEN_HEIGHT, x, sprite_sheet, scale, y = 0):
        pygame.sprite.Sprite.__init__(self)
        
        # animation
        self.animation_list = []
        self.frame_index = 0
        self.last_update_time = pygame.time.get_ticks()
        self.ANIMATIONS = 60
        
        # load image animation
        for animation_index in range(1, self.ANIMATIONS + 1):
            image = sprite_sheet.get_image(animation_index, 34, 30, scale, (0, 0, 0))
            image = pygame.transform.flip(image, flip_x = True, flip_y = False)
            image.set_colorkey((0, 0, 0))
            self.animation_list.append(image)
        
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def update(self, scroll = 0, SCREEN_HEIGHT = 600):
        ANIMATION_COOLDOWN = 1000/60 #ms
        
        self.image = self.animation_list[self.frame_index]
        if (pygame.time.get_ticks() - self.last_update_time) > ANIMATION_COOLDOWN:
            self.last_update_time = pygame.time.get_ticks()
            self.frame_index = (self.frame_index + 1) % self.ANIMATIONS
        
        # move object
        # self.rect.x += self.direction * 2
        self.rect.y += scroll + 2

        # isOffScreen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255,255,255), self.rect, 2)