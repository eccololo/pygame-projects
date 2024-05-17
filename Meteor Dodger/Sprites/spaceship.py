import pygame


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos):
        super().__init__()
        
        # Creating surface
        self.image = pygame.image.load(path)
        # Create rectangle
        self.rect = self.image.get_rect(center=(x_pos, y_pos))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.__screen_constrain()

    def __screen_constrain(self):
        if self.rect.right >= 1280:
            self.rect.right = 1280

        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= 720:
            self.rect.bottom = 720


