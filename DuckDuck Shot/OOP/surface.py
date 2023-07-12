import pygame


class Surface:

    def __init__(self, img_path, screen):
        self.surface = pygame.image.load(img_path)
        self.screen = screen

        # For animation y
        self.animation_start_y = None
        self.animation_max_y = None
        self.animation_min_y = None
        self.animation_speed = None

        # For animation x
        self.animation_start_x = None
        self.animation_max_x = None
        self.animation_min_x = None
        self.animation_speed = None

    def display_surface(self, x_cor, y_cor):
        self.screen.get_screen().blit(self.surface, (x_cor, y_cor))

    def make_animable_y(self, animation_start_y=None, animation_max_y=None, animation_min_y=None, animation_speed=None):
        self.animation_start_y = animation_start_y
        self.animation_max_y = animation_max_y
        self.animation_min_y = animation_min_y
        self.animation_speed = animation_speed

    def make_animable_x(self, animation_start_x=None, animation_max_x=None, animation_min_x=None, animation_speed=None):
        self.animation_start_x = animation_start_x
        self.animation_max_x = animation_max_x
        self.animation_min_x = animation_min_x
        self.animation_speed = animation_speed

    def animate_y(self, x_cor):
        self.animation_start_y += self.animation_speed
        if self.animation_start_y >= self.animation_max_y or self.animation_start_y <= self.animation_min_y:
            self.animation_speed *= -1
        self.screen.get_screen().blit(self.surface, (x_cor, self.animation_start_y))

    def animate_x(self, y_cor):
        self.animation_start_x += self.animation_speed
        if self.animation_start_x >= self.animation_max_x or self.animation_start_x <= self.animation_min_x:
            self.animation_speed *= -1
        self.screen.get_screen().blit(self.surface, (y_cor, self.animation_start_x))
