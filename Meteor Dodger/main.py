import pygame, sys
import random
from Sprites.spaceship import SpaceShip
from Sprites.meteor import Meteor
from Sprites.laser import Laser
from settings import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def main_game():
    # Sprites Render
    laser_group.draw(screen)
    laser_group.update()
    spaceship_group.draw(screen)
    spaceship_group.update()
    meteor_group.draw(screen)
    meteor_group.update()

    # Collisions
    if pygame.sprite.spritecollide(spaceship_group.sprite, meteor_group, True):
        spaceship_group.sprite.get_damage(1)

    for laser in laser_group:
        pygame.sprite.spritecollide(laser, meteor_group, True)

def end_game():
    game_font = pygame.font.Font(None, 100)
    game_font_surface = game_font.render('Game Over!', True, (255, 255, 255), (45, 48, 51))
    game_font_rect = game_font_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(game_font_surface, game_font_rect)

# TODO:
#    1. Create possibility for user to enter his prefered game difficulty in game screen.
# user_diff_choice = input()
user_diff_choice = "easy"

spaceship = SpaceShip('./assets/sprites/spaceship.png', './assets/sprites/shield.png', 640, 500)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)


# For creating multiple meteors on screen.
METEOR_EVENT = pygame.USEREVENT
pygame.time.set_timer(METEOR_EVENT, DIFFICULTY_LEVEL[user_diff_choice])

meteor_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == METEOR_EVENT:
            meteor_image = random.choice(['./assets/sprites/Meteor1.png', './assets/sprites/Meteor2.png', './assets/sprites/Meteor3.png'])
            random_pos_x = random.randint(0, 1200)
            random_pos_y = random.randint(-500, -50)
            speed_x = random.randrange(-1, 1)
            speed_y = random.randrange(3, 10)
            meteor_group.add(Meteor(meteor_image, random_pos_x, random_pos_y, speed_x, speed_y))
        if event.type == pygame.MOUSEBUTTONDOWN:
            laser_image = './assets/sprites/Laser.png'
            laser_group.add(Laser(laser_image, event.pos, 14))

    screen.fill((45, 48, 51))

    if spaceship_group.sprite.health > 0:
        main_game()
    else:
        end_game()

    pygame.display.update()
    clock.tick(120)