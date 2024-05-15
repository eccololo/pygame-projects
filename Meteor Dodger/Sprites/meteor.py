import pygame


class Meteor(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, speed_x, speed_y):
        super().__init__()
        
        # Creating surface
        self.image = pygame.image.load(path)
        # Create rectangle
        self.rect = self.image.get_rect(center=(x_pos, y_pos))

        self.rect.x = x_pos
        self.rect.y = y_pos

        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.centerx += self.speed_x
        self.rect.centery += self.speed_y

        # Saving computer resources that game can work smoothly.
        if self.rect.centery > 700:
            self.kill()
