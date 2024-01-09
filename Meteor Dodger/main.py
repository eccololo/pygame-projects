import pygame, sys
from spaceship import SpaceShip

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

spaceship = SpaceShip('./assets/sprites/spaceship.png', 640, 500, 10)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((45, 48, 51))
    spaceship_group.draw(screen)
    spaceship_group.update()
    pygame.display.update()
    clock.tick(120)