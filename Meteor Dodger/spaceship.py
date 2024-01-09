import pygame


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__()
        # Creating surface
        self.image = pygame.image.load(path)
        # Create rectangle
        self.rect = self.image.get_rect(center=(x_pos, y_pos))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def screen_constrain(self):

