import pygame


class Surface:

    def __init__(self, img_path, screen, x_cor, y_cor):
        self.surface = pygame.image.load(img_path)
        self.screen = screen

        self.x_cor = x_cor
        self.y_cor = y_cor

        # For animation y
        self.animation_start_y = None
        self.animation_max_y = None
        self.animation_min_y = None
        self.animation_speed_y = None

        # For animation x
        self.animation_start_x = None
        self.animation_max_x = None
        self.animation_min_x = None
        self.animation_speed_x = None

    def display_surface(self, surface_obj=None):
        if surface_obj:
            self.screen.get_screen().blit(surface_obj, (surface_obj.x_cor, surface_obj.y_cor))
        else:
            self.screen.get_screen().blit(self.surface, (self.x_cor, self.y_cor))

    def make_animable_y(self, animation_max_y, animation_min_y, animation_speed_y):
        self.animation_start_y = self.y_cor
        self.animation_max_y = animation_max_y
        self.animation_min_y = animation_min_y
        self.animation_speed_y = animation_speed_y

    def make_animable_x(self, animation_max_x, animation_min_x, animation_speed_x):
        self.animation_start_x = self.x_cor
        self.animation_max_x = animation_max_x
        self.animation_min_x = animation_min_x
        self.animation_speed_x = animation_speed_x

    def animate_y(self):
        self.animation_start_y += self.animation_speed_y
        if self.animation_start_y >= self.animation_max_y or self.animation_start_y <= self.animation_min_y:
            self.animation_speed_y *= -1
        self.screen.get_screen().blit(self.surface, (self.x_cor, self.animation_start_y))

    def animate_x(self):
        self.animation_start_x += self.animation_speed_x
        if self.animation_start_x >= self.animation_max_x or self.animation_start_x <= self.animation_min_x:
            self.animation_speed_x *= -1
        self.screen.get_screen().blit(self.surface, (self.animation_start_x, self.y_cor))
