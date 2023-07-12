import pygame
from screen import Screen
from surface import Surface

pygame.init()
screen = Screen()

# ============= Surface Assets ===============
wood_bg = Surface("./assets/images/Wood_BG.png", screen)
land_bg = Surface("./assets/images/Land_BG.png", screen)
water_bg = Surface("./assets/images/Water_BG.png", screen)
cloud_1 = Surface("./assets/images/Cloud1.png", screen)
cloud_2 = Surface("./assets/images/Cloud2.png", screen)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen.quit_game()

    wood_bg.display_surface(0, 0)

    pygame.display.update()
    screen.set_clock(120)