import pygame

class WeaponSpritesheet():
    def __init__(self, folder_name):
        self.directory = folder_name

    def get_image(self, frame, width, height, scale, colour):
        img = pygame.image.load('{}/{}.png'.format(self.directory, frame)).convert_alpha()
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(source = img, dest = (0, 0))#, area = ((width), 0, width, height))
        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        image.set_colorkey(colour)
        return image