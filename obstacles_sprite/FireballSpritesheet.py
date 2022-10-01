import pygame

class FireballSpriteSheet():
    def __init__(self, image):
        self.image = image
    
    def get_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.image, (0, 0), ((width, 0, width, height)))
        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        image.set_colorkey(colour)
        return image