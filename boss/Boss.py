import pygame
import random

class Boss(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, y, sprite_sheet, scale):
        pygame.sprite.Sprite.__init__(self)
        
        # movement
        self.direction = random.choice([-1, 1])
        self.flip = True if self.direction == -1 else False
        
        # animation
        self.animation_list = []
        self.frame_index = 0
        self.last_update_time = pygame.time.get_ticks()
        self.ANIMATIONS = 2
        
        # load image animation
        for animation_index in range(1, self.ANIMATIONS + 1):
            image = sprite_sheet.get_image(animation_index, 32, 32, scale, (0, 0, 0))
            image = pygame.transform.flip(image, flip_x = self.flip, flip_y = False)
            image.set_colorkey((0, 0, 0))
            self.animation_list.append(image)
        
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = 0 if self.direction == 1 else SCREEN_WIDTH
        self.rect.y = y
    
    def update(self, scroll = 0, SCREEN_WIDTH = 400):
        # Update animation
        ANIMATION_COOLDOWN = 50

        # Update image depending on current frame
        self.image = self.animation_list[self.frame_index]

        # Check if enough time has passed since the last update
        if (pygame.time.get_ticks() - self.last_update_time) > ANIMATION_COOLDOWN:
            self.last_update_time = pygame.time.get_ticks()
            self.frame_index = (self.frame_index + 1) % self.ANIMATIONS
        
        # Move boss
        self.rect.x += self.direction * 2
        self.rect.y += scroll

        # Check if boss is off screen
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()