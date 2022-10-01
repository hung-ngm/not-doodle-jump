import pygame
import random
import os
from enum import Enum
from pygame import mixer
from constant import *
from edge.platform import *
from obstacles_sprite.Bluebird import *
from obstacles_sprite.BluebirdSpritesheet import *
from obstacles_sprite.Fireball import *
from obstacles_sprite.FireballSpritesheet import *
from boss.Boss import *
from boss.BossSpritesheet import *
from minion.Minion import *
from minion.MinionSpritesheet import *
from weapon.Weapon import *
from weapon.WeaponSpritesheet import *

"""
    Initialise pygame
"""
mixer.init()
pygame.init()

"""
    CONSTANTS
"""
#sounds
jump_fx = pygame.mixer.Sound('assets/sfx/jump.mp3')
jump_fx.set_volume(0.5)
death_fx = pygame.mixer.Sound('assets/sfx/death.mp3')
death_fx.set_volume(0.5)
hit_fx = pygame.mixer.Sound('assets/sfx/hit.wav')
hit_fx.set_volume(0.5)
# create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('HHH')

# Game variables
scroll = 0
bg_scroll = 0
game_over = False
score = 0
fade_counter = 0

if os.path.exists('score.txt'):
    with open('score.txt', 'r') as file:
	    high_score = int(file.read())
else:
	high_score = 0

# Font 
font_small = pygame.font.SysFont('Pixeloid', 20)
font_big = pygame.font.SysFont('Pixeloid', 24)

"""
    VARIABLES
"""
# Game variables
score = 0

# Set frame rate 
clock = pygame.time.Clock()
last_attack = pygame.time.get_ticks()
# Load music and sounds

# Load images
bg_image = pygame.image.load('assets/gfx/bg.png').convert_alpha()
platform_image = pygame.image.load('assets/gfx/wood.png').convert_alpha()
player_image = pygame.image.load('assets/gfx/player.png').convert_alpha()

"""
    DRAW
"""

#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

#function for drawing info panel
def draw_panel():
	pygame.draw.rect(screen, PANEL, (0, 0, SCREEN_WIDTH, 30))
	pygame.draw.line(screen, WHITE, (0, 30), (SCREEN_WIDTH, 30), 2)
	draw_text('SCORE: ' + str(score), font_small, WHITE, 0, 0)

#function for drawing the background
def draw_bg(bg_scroll):
	screen.blit(bg_image, (0, 0 + bg_scroll))
	screen.blit(bg_image, (0, -600 + bg_scroll))

"""
    PLAYER
"""
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.transform.scale(player_image, (45, 45))
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip = False
    
    def move(self, score):
        #reset movement variables
        dx = 0
        dy = 0
        scroll = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx -= HORIZONTAL_SPEED
            self.flip = True
        if key[pygame.K_RIGHT]:
            dx += HORIZONTAL_SPEED
            self.flip = False
        
        if (score >= BOSS_LEVEL_SCORE):
            if key[pygame.K_UP]:
                dy -= VERTICAL_SPEED

        self.vel_y += GRAVITY
        dy += self.vel_y

        #check for collision with platforms
        for platform in platform_group:
            #collision in the y direction
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                #check if above platform
                if self.rect.bottom < platform.rect.centery:
                    if self.vel_y > 0:
                        self.rect.bottom = platform.rect.top
                        dy = 0
                        self.vel_y = -20
                        if (score > BOSS_LEVEL_SCORE):
                            self.vel_y = 0

        #check if player hit top of screen
        if self.rect.top <= SCROLL_THRESH:
            # If player is jumping
            if self.vel_y < 0:
                scroll = -dy

        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy + scroll

		#update mask
        self.mask = pygame.mask.from_surface(self.image)

        return scroll

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 12, self.rect.y - 5))
        
"""
    Instances and sprite
"""
#player instance
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

# platform group 
platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, False, platform_image)
platform_group = pygame.sprite.Group()
platform_group.add(platform)   

# obstacles groups
bluebird_spritesheet = BluebirdSpritesheet('assets/obstacles/Bluebird')
bluebird_group = pygame.sprite.Group()
fireball_spritesheet = FireballSpritesheet('assets/obstacles/Fireball')
fireball_group = pygame.sprite.Group()

# boss
boss_spritesheet = BossSpritesheet('assets/boss/Boss')
boss_group = pygame.sprite.Group()

# minion
minion_spritesheet = MinionSpritesheet('assets/minion/Minion')
minion_group = pygame.sprite.Group()

# weapon 
weapon_spritesheet = WeaponSpritesheet('assets/weapon')
weapon_group = pygame.sprite.Group()
"""
    GAME
"""
# beginning = True
run = True
beginning = True
while run:
    clock.tick(FPS)    
    if beginning:
        boss_group.empty()
        bluebird_group.empty()
        fireball_group.empty()
        weapon_group.empty()
        minion_group.empty()
        beginning = False

    if game_over == False:
        scroll = player.move(score)

        # draw background
        bg_scroll += scroll
        if bg_scroll >= 600:
            bg_scroll = 0
        draw_bg(bg_scroll)

        # Generate platforms
        if (len(platform_group) < MAX_PLATFORMS):
            p_w = random.randint(PLATFORM_MIN_WIDTH, PLATFORM_MAX_WIDTH)
            p_x = random.randint(0, SCREEN_WIDTH - p_w)
            p_y = platform.rect.y - random.randint(PLATFORM_MIN_HEIGHT_DIFF, PLATFORM_MAX_HEIGHT_DIFF)
            # Type 1 for moving platforms, type 2 for static platforms
            p_type = random.randint(1, 2)

            if p_type == 1 and score > 500:
                p_moving = True
            else:
                p_moving = False
            platform = Platform(p_x, p_y, p_w, p_moving, platform_image)
            platform_group.add(platform)

        #update platforms
        platform_group.update(scroll)

        # Generate obstacles
        if len(bluebird_group) == 0:
            bluebird = Bluebird(SCREEN_WIDTH, 100, bluebird_spritesheet, 1.5)
            bluebird_group.add(bluebird)
        
        if len(fireball_group) == 0:
            fireball = Fireball(SCREEN_HEIGHT, random.randint(32, SCREEN_WIDTH - 32), fireball_spritesheet, 1.5)
            fireball_group.add(fireball)

        
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if (pygame.time.get_ticks() - last_attack) >= ATTACK_COOLDOWN:
                last_attack = pygame.time.get_ticks()
                weapon = Weapon(SCREEN_HEIGHT, 
                                player.rect.x,
                                player.rect.y - 10, 
                                weapon_spritesheet, 0.5)
                weapon_group.add(weapon)
        
        # Update group
        bluebird_group.update(scroll, SCREEN_WIDTH)
        platform_group.update(scroll)
        fireball_group.update(scroll, SCREEN_HEIGHT)
        weapon_group.update(scroll, SCREEN_HEIGHT)
       
        #update score
        if scroll > 0:
            score += scroll
            
        # Boss level
        if score >= BOSS_LEVEL_SCORE:
            platform_group.empty()
            bluebird_group.empty()

            # Reset sprites
            platform = Platform(0, SCREEN_HEIGHT - 10, SCREEN_WIDTH, False, platform_image)
            platform_group.add(platform)

            if len(boss_group) == 0:
                boss = Boss(SCREEN_WIDTH, 0, boss_spritesheet, 1.5)
                boss_group.add(boss)
            
            if len(minion_group) == 0:
                minion1 = Minion(SCREEN_WIDTH, 160, minion_spritesheet, 1, 1.5)
                minion2 = Minion(SCREEN_WIDTH, 210, minion_spritesheet, -1, 1.5)
                minion_group.add(minion1)
                minion_group.add(minion2)
            
            if len(fireball_group) < MAX_FIREBALLS: 
                new_fireball = Fireball(SCREEN_HEIGHT, random.randint(32, SCREEN_WIDTH - 32), fireball_spritesheet, 1.5)
                fireball_group.add(new_fireball)

            keys=pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                if (pygame.time.get_ticks() - last_attack) >= ATTACK_COOLDOWN:
                    last_attack = pygame.time.get_ticks()
                    weapon = Weapon(SCREEN_HEIGHT, 
                                    player.rect.x,
                                    player.rect.y - 10, 
                                    weapon_spritesheet, 0.5)
                    weapon_group.add(weapon)

            # Update group
            boss_group.update()
            platform_group.update(scroll)
            bluebird_group.update(scroll, SCREEN_WIDTH)
            fireball_group.update(scroll, SCREEN_HEIGHT)
            weapon_group.update(scroll, SCREEN_HEIGHT)
            minion_group.update(scroll, SCREEN_WIDTH)

            #update score
            if scroll > 0:
                score += scroll

        # Draw panel
        if (score < BOSS_LEVEL_SCORE):
            draw_panel()
        
        # Draw sprites
        platform_group.draw(screen)
        bluebird_group.draw(screen)
        fireball_group.draw(screen)
        boss_group.draw(screen)
        weapon_group.draw(screen)
        minion_group.draw(screen)
        player.draw()

        # Check game over
        if player.rect.top > SCREEN_HEIGHT:
            game_over = True
            death_fx.play()
        
        # Check collision
        # if pygame.sprite.spritecollide(player, bluebird_group, False):
        #     if pygame.sprite.spritecollide(player, bluebird_group, False, pygame.sprite.collide_mask):
        #         game_over = True
        #         death_fx.play()

        if pygame.sprite.spritecollide(player, fireball_group, False):
            if pygame.sprite.spritecollide(player, fireball_group, False, pygame.sprite.collide_mask):
                game_over = True
                death_fx.play()
        
        if pygame.sprite.groupcollide(bluebird_group, weapon_group, True, True):
            hit_fx.play()
        
        if pygame.sprite.groupcollide(boss_group, weapon_group, False, True):
            hit_fx.play()
            boss.health -= 1
            if boss.health == 0:
                boss.kill()
                boss_group.empty()
                
    else:
        # Play again screen
        if fade_counter < SCREEN_WIDTH:
            fade_counter += 5
            for y in range(0, 6, 2):
                pygame.draw.rect(screen, BLACK, (0, y * 100, fade_counter, 100))
                pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH - fade_counter, (y + 1) * 100, SCREEN_WIDTH, 100))
        
        else:
            draw_text('GAME OVER!', font_big, WHITE, 150, 200)
            draw_text('SCORE: ' + str(score), font_big, WHITE, 155, 250)
            draw_text('PRESS ENTER TO PLAY AGAIN', font_big, WHITE, 65, 300)
			
            # Update high score
            if score > high_score:
                high_score = score
                with open('score.txt', 'w') as file:
                    file.write(str(high_score))
            key = pygame.key.get_pressed()
            if key[pygame.K_RETURN]:
                # Reset variables
                game_over = False
                score = 0
                scroll = 0
                fade_counter = 0
                beginning = True
                # Reset the position of the player
                player.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

                # Reset the enemies
                bluebird_group.empty()

                # Reset the platforms
                platform_group.empty()

                # Create starting platform
                platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, False, platform_image)
                platform_group.add(platform)


    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # update display window
    pygame.display.update()
    
pygame.quit()
