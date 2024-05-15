import random
from settings import SCREEN_WIDTH


class Generator:

    def __init__(self, game_obj, num_of_obj):
        self.game_object_list = []
        self.game_obj = game_obj
        self.num_of_obj = num_of_obj

    def gen_game_objects(self):
        for _ in range(self.num_of_obj):
            self.game_obj.x_cor = random.randrange(50, SCREEN_WIDTH - 90)
            self.game_obj.y_cor = random.randrange(30, 130)
            self.game_object_list.append(self.game_obj)

        return self.game_object_list

    def get_game_obj_list(self):
        return self.game_object_list
