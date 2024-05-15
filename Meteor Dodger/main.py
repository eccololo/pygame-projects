import pygame, sys
import random
from Sprites.spaceship import SpaceShip
from Sprites.meteor import Meteor
from settings import *

pygame.init()
screen = pygame.display.set_mode((1200, 640))
clock = pygame.time.Clock()

# TODO:
#    1. Create possibility for user to enter his prefered game difficulty in game screen.
# user_diff_choice = input()

spaceship = SpaceShip('./assets/sprites/spaceship.png', 640, 500, 10)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

# For creating multiple meteors on screen.
METEOR_EVENT = pygame.USEREVENT
pygame.time.set_timer(METEOR_EVENT, DIFFICULTY_LEVEL[user_diff_choice])

meteor_group = pygame.sprite.Group()
    

print(len(meteor_group))

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

    screen.fill((45, 48, 51))
    
    # Sprites
    spaceship_group.draw(screen)
    spaceship_group.update()
    meteor_group.draw(screen)
    meteor_group.update()

    pygame.display.update()
    clock.tick(120)