import pygame


class Surface:

    def __init__(self, img_path, screen):
        self.surface = pygame.image.load(img_path)
        self.screen = screen

    def display_surface(self, x_cor, y_cor):
        self.screen.get_screen().blit(self.surface, (x_cor, y_cor))
