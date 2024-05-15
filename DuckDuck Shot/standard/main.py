import pygame
import sys
import random
from settings import *


def gen_ducks(game_lvl):
    d_list = []
    ducks_to_gen = NUM_OF_DUCKS + game_lvl
    if ducks_to_gen > MAX_NUM_OF_DUCKS:
        ducks_to_gen = MAX_NUM_OF_DUCKS
    for _ in range(ducks_to_gen):
        duck_position_x = random.randrange(50, SCREEN_WIDTH - 90)
        duck_position_y = random.randrange(200, 390)
        duck_rectangle = duck_surface.get_rect(center=(duck_position_x, duck_position_y))
        d_list.append(duck_rectangle)
    return d_list


def gen_clouds():
    c_list = []
    for _ in range(NUM_OF_CLOUDS):
        cloud_position_x = random.randrange(50, SCREEN_WIDTH - 90)
        cloud_position_y = random.randrange(30, 130)
        cloud_choice = random.choice([cloud_1, cloud_2])
        cloud_item = (cloud_choice, cloud_position_x, cloud_position_y)
        c_list.append(cloud_item)
    return c_list


def update_game_time():
    global GAME_LEVEL_UPDATE_TIME
    GAME_LEVEL_UPDATE_TIME = int(GAME_LEVEL_UPDATE_TIME) - 1
    game_level_time = GAME_LEVEL_UPDATE_TIME
    if game_level_time < 10:
        game_level_time = "0" + str(game_level_time)
    game_time_ctd = game_time.render(f"0:{game_level_time}", True, (255, 255, 255))
    return game_time_ctd


def quit_game():
    pygame.display.quit()
    pygame.quit()
    sys.exit()


def clear_game_objects():
    duck_list.clear()
    cloud_list.clear()


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DuckDuck Shooter Game.")
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

# ================== Music ==================
shot_music = pygame.mixer.Sound("./assets/sounds/game-gun-shot.mp3")
background_music = pygame.mixer.Sound("./assets/sounds/atmosphere-of-a-river-at-sunrise.wav")
next_level_music = pygame.mixer.Sound("./assets/sounds/casino-bling-achievement.wav")
game_level_completed_music = pygame.mixer.Sound("./assets/sounds/game-level-completed-1.wav")
game_over_music = pygame.mixer.Sound("./assets/sounds/melodic-game-over-1.wav")
background_music.play()

# ================== Assets ==================
wood_bg = pygame.image.load("./assets/images/Wood_BG.png")
land_bg = pygame.image.load("./assets/images/Land_BG.png")
water_bg = pygame.image.load("./assets/images/Water_BG.png")
cloud_1 = pygame.image.load("./assets/images/Cloud1.png")
cloud_2 = pygame.image.load("./assets/images/Cloud2.png")
crosshair = pygame.image.load("./assets/images/crosshair.png")
duck_surface = pygame.image.load("./assets/images/duck.png")

# ================== Animation ==================
land_position_y = 480
water_position_y = 420
land_animation_speed = 0.3
water_animation_speed = 0.6

# ================== Text ==================
hits = 0
game_font = pygame.font.Font(None, 33)
game_level = pygame.font.Font(None, 33)
game_time = pygame.font.Font(None, 33)
win_font = pygame.font.Font(None, 100)
end_font = pygame.font.Font(None, 100)
text_surface = game_font.render(f"Hits: {hits}", True, (255, 255, 255))
game_level_surface = game_font.render(f"Level: {GAME_LEVEL}", True, (255, 255, 255))
game_win_surface = win_font.render("You Won!", True, (255, 255, 255))
game_over_surface = end_font.render("Game Over!", True, (255, 255, 255))
game_time_countdown = update_game_time()

crosshair_rect = crosshair.get_rect(center=(640, 360))

# ================== Game Objects ==================
duck_list = gen_ducks(GAME_LEVEL)
cloud_list = gen_clouds()
timer_counter = 0

while True:
    timer_counter += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center=event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            shot_music.play()
            ducks_idx_to_del = []
            for idx, duck_rect in enumerate(duck_list):
                if crosshair_rect.colliderect(duck_rect):
                    ducks_idx_to_del.append(idx)  # Fix to delete only 1 duck that is on the top
            if len(ducks_idx_to_del) > 0:
                max_idx = max(ducks_idx_to_del)
                del duck_list[max_idx]
                hits += 1
                text_surface = game_font.render(f"Hits: {hits}", True, (255, 255, 255))

    screen.blit(wood_bg, (0, 0))

    water_position_y += water_animation_speed
    if water_position_y >= 450 or water_position_y <= 390:
        water_animation_speed *= -1
    screen.blit(water_bg, (0, water_position_y))

    land_position_y += land_animation_speed
    if land_position_y >= 500 or land_position_y <= 460:
        land_animation_speed *= -1
    screen.blit(land_bg, (0, land_position_y))

    for duck_rect in duck_list:
        screen.blit(duck_surface, duck_rect)

    for cloud in cloud_list:
        screen.blit(cloud[0], (cloud[1], cloud[2]))

    # ============== TEXT Objects ===============
    screen.blit(game_level_surface, (15, 15))
    screen.blit(text_surface, (15, 45))

    if (timer_counter % 120 == 0 and not IS_GAME_OVER) and (timer_counter % 120 == 0 and not GAME_WON):
        game_time_countdown = update_game_time()
    screen.blit(game_time_countdown, (SCREEN_WIDTH - 60, 15))

    screen.blit(crosshair, crosshair_rect)

    # NEXT LEVEL
    if not GAME_WON and not IS_GAME_OVER:
        if len(duck_list) <= 0:
            GAME_LEVEL += 1
            duck_list = gen_ducks(GAME_LEVEL)
            if GAME_LEVEL % 3 == 0:
                cloud_list = gen_clouds()
            IS_NEXT_LVL = True
            game_level_surface = game_font.render(f"Level: {GAME_LEVEL}", True, (255, 255, 255))
            if IS_NEXT_LVL:
                GAME_LEVEL_UPDATE_TIME = GAME_LEVEL_START_TIME + int(GAME_LEVEL * 0.5)
                if GAME_LEVEL % 5 == 0:
                    game_level_completed_music.play()
                else:
                    next_level_music.play()
                IS_NEXT_LVL = False

    # GAME OVER
    if GAME_LEVEL_UPDATE_TIME <= 0:
        IS_GAME_OVER = True
        GAME_LEVEL_UPDATE_TIME = 1
        if IS_GAME_OVER:
            game_over_music.play()

    # END GAME
    if GAME_LEVEL >= MAX_GAME_LVL:
        GAME_WON = True
        clear_game_objects()
        screen.blit(game_win_surface, (int(SCREEN_WIDTH / 2) - 150, int(SCREEN_HEIGHT / 2) - 40))
        if timer_counter % (120 * 5) == 0:
            quit_game()

    if IS_GAME_OVER:
        clear_game_objects()
        screen.blit(game_over_surface, (int(SCREEN_WIDTH / 2) - 190, int(SCREEN_HEIGHT / 2) - 40))
        if timer_counter % (120 * 5) == 0:
            quit_game()

    pygame.display.update()
    clock.tick(120)
