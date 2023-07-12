import pygame
from screen import Screen
from surface import Surface

pygame.init()
screen = Screen()

# ============= Surface Assets ===============
wood_bg = Surface("./assets/images/Wood_BG.png", screen)

land_bg = Surface("./assets/images/Land_BG.png", screen)
land_bg.make_animable_y(480, 500, 460, 0.3)
water_bg = Surface("./assets/images/Water_BG.png", screen)
water_bg.make_animable_y(420, 450, 390, 0.6)

cloud_1 = Surface("./assets/images/Cloud1.png", screen)
cloud_1.make_animable_x(100, 112, 97, 0.2)
cloud_2 = Surface("./assets/images/Cloud2.png", screen)
cloud_2.make_animable_x(500, 510, 490, 0.2)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen.quit_game()

    wood_bg.display_surface(0, 0)
    water_bg.animate_y(0)
    land_bg.animate_y(0)
    cloud_1.animate_x(60)
    cloud_2.animate_x(120)

    pygame.display.update()
    screen.set_clock(120)