import random
from typing import Tuple

class Circle:
    def __init__(self, grid_size: Tuple[int, int]):
        self.position = self.generate_new_position(grid_size)

    def generate_new_position(self, grid_size: Tuple[int, int]) -> Tuple[int, int]:
        x = random.randint(0, grid_size[0] - 1)
        y = random.randint(0, grid_size[1] - 1)
        return x, y
