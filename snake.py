from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Snake:
    position: List[Tuple[int, int]]
    direction: str

    def __init__(self, grid_size: Tuple[int, int]):
        self.position = [(grid_size[0] // 2, grid_size[1] // 2)]
        self.direction = "RIGHT"

    def move(self):
        head = self.position[0]
        x, y = head

        if self.direction == "UP":
            y -= 1
        elif self.direction == "DOWN":
            y += 1
        elif self.direction == "LEFT":
            x -= 1
        elif self.direction == "RIGHT":
            x += 1

        self.position.insert(0, (x, y))
        self.position.pop()

    def change_direction(self, new_direction: str):
        if new_direction == "UP" and self.direction != "DOWN":
            self.direction = new_direction
        elif new_direction == "DOWN" and self.direction != "UP":
            self.direction = new_direction
        elif new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = new_direction
        elif new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = new_direction

    def check_collision(self, grid_size: Tuple[int, int]) -> bool:
        head = self.position[0]
        x, y = head

        if x < 0 or x >= grid_size[0] or y < 0 or y >= grid_size[1]:
            return True

        if head in self.position[1:]:
            return True

        return False

    def collides_with(self, position: Tuple[int, int]) -> bool:
        return position in self.position

    def grow(self):
        tail = self.position[-1]
        self.position.append(tail)
