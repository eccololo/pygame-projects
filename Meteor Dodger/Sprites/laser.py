import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, path, pos, speed):
        super().__init__()
        
        # Creating surface
        self.image = pygame.image.load(path)
        # Create rectangle
        self.rect = self.image.get_rect(center=pos)

        self.speed = speed

    def update(self):
        self.rect.centery -= self.speed
        if self.rect.centery <= -100:
            self.kill()