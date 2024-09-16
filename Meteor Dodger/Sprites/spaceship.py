import pygame


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, path_spaceship_image, path_shield_image, x_pos, y_pos):
        super().__init__()
        
        self.discharged = pygame.image.load(path_spaceship_image)
        self.charged = pygame.image.load("./assets/sprites/spaceship_charged.png")

        # Creating surface
        self.image = self.discharged
        self.shiled_surface = pygame.image.load(path_shield_image)
        # Create rectangle
        self.rect = self.image.get_rect(center=(x_pos, y_pos))

        self.health = 5

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.__screen_constrain()
        self.display_health()

    def __screen_constrain(self):
        if self.rect.right >= 1280:
            self.rect.right = 1280

        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= 720:
            self.rect.bottom = 720

    def display_health(self):
        for idx, shield in enumerate(range(self.health)):
            pygame.display.get_surface().blit(self.shiled_surface, (idx * 40 + 10, 10))

    def get_damage(self, damage_amount):
        self.health -= damage_amount

    def charge(self):
        self.image = self.charged

    def discharge(self):
        self.image = self.discharged
