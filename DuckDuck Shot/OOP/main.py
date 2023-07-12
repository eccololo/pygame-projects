import pygame
from screen import Screen

pygame.init()
screen = Screen()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen.quit_game()

    pygame.display.update()
    screen.set_clock(120)