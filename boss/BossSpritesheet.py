import pygame

class BossSpritesheet():
	def __init__(self, folder_name):
		self.directory = folder_name

	def get_image(self, frame, width, height, scale, colour):
		STARTING_X_PIXEL_OF_BOSS = 50
		STARTING_Y_PIXEL_OF_BOSS = 14
		img = pygame.image.load('{}/{}.png'.format(self.directory, frame)).convert_alpha()
		image = pygame.Surface((width, height)).convert_alpha() # Surface
		image.blit(
      		source = img, 
        	dest = (0, 0), 
            area = (STARTING_X_PIXEL_OF_BOSS, STARTING_Y_PIXEL_OF_BOSS, width, height)
        )
		image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		image.set_colorkey(colour)
		return image