from enum import Enum
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
PLATFORM_HEIGHT = 10
MAX_PLATFORMS = 10
PLATFORM_MIN_WIDTH = 40
PLATFORM_MAX_WIDTH = 70
PLATFORM_MIN_HEIGHT_DIFF = 80
PLATFORM_MAX_HEIGHT_DIFF = 120

# Speed
HORIZONTAL_SPEED = 10
VERTICAL_SPEED = 10
GRAVITY = 1

#game variables
SCROLL_THRESH = 200
MAX_PLATFORMS = 10

# Weapon 
WEAPON_MENU = Enum("SWORD", "SHURIKEN", "FIRE")