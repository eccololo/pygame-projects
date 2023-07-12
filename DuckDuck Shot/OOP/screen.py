import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Screen:

    def __init__(self):
        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("DuckDuck Shooter Game.")
        pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()

    def get_clock(self):
        return self.clock

    def set_clock(self, fps):
        self.clock.tick(fps)

    @staticmethod
    def quit_game():
        pygame.quit()
        sys.exit()
