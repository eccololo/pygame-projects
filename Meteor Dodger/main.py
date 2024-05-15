import pygame, sys
import random
from Sprites.spaceship import SpaceShip
from Sprites.meteor import Meteor
from settings import *

pygame.init()
screen = pygame.display.set_mode((1200, 640))
clock = pygame.time.Clock()

spaceship = SpaceShip('./assets/sprites/spaceship.png', 640, 500, 10)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

for _ in range(METEORS_NUM):
    random_x = random.randint(200, 800)
    random_y = random.randint(100, 300)
    speed_x = random.choice([-2, -1, 1, 2])
    speed_y = random.choice([-2, -1, 1 ,2])
    meteor_group = pygame.sprite.Group()
    meteor_group.add(Meteor('./assets/sprites/meteor1.png', random_x, random_y, speed_x, speed_y))

print(len(meteor_group))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((45, 48, 51))
    
    # Sprites
    spaceship_group.draw(screen)
    spaceship_group.update()
    meteor_group.draw(screen)
    meteor_group.update()

    pygame.display.update()
    clock.tick(120)