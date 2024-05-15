import pygame
from screen import Screen
from surface import Surface
from cloud import Cloud
from generator import Generator
from settings import *

pygame.init()
screen = Screen()

# ============= Surface Assets ===============
wood_bg = Surface("./assets/images/Wood_BG.png", screen, 0, 0)

land_bg = Surface("./assets/images/Land_BG.png", screen, 0, 480)
land_bg.make_animable_y(500, 460, 0.3)
water_bg = Surface("./assets/images/Water_BG.png", screen, 0, 420)
water_bg.make_animable_y(450, 390, 0.6)

cloud_1 = Cloud("./assets/images/Cloud1.png", screen)
clouds_list_1 = Generator(cloud_1, NUM_OF_CLOUDS).gen_game_objects()
cloud_2 = Cloud("./assets/images/Cloud2.png", screen)
clouds_list_2 = Generator(cloud_2, NUM_OF_CLOUDS).gen_game_objects()

clouds_list = clouds_list_1 + clouds_list_2

cloud_2.make_animable_x(500, 510, 490)
cloud_1.make_animable_x(100, 112, 97)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen.quit_game()

    wood_bg.display_surface()

    water_bg.animate_y()
    land_bg.animate_y()

    for cloud in clouds_list:
        cloud.display_surface(cloud)
    # cloud_1.animate_x()
    # cloud_2.animate_x()

    pygame.display.update()
    screen.set_clock(120)