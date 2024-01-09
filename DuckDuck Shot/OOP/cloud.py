from surface import Surface
from random import randint


class Cloud(Surface):

    def __init__(self, img_path, screen, x_cor=0, y_cor=0):
        super().__init__(img_path, screen, x_cor, y_cor)

    def randomize_cloud_pos(self):
        self.x_cor = randint(50, 800)
        self.y_cor = randint(0, 300)
