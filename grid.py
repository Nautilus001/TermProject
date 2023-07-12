import pygame
from typing import Tuple

class Grid:
    def __init__(self, size: Tuple[int, int]):
        self.size = size
        self.cell_size = 40  # Adjust the cell size here

    def get_screen_size(self) -> Tuple[int, int]:
        return self.size[0] * self.cell_size, self.size[1] * self.cell_size

    def draw(self, screen):
        for x in range(0, self.size[0] * self.cell_size, self.cell_size):
            pygame.draw.line(screen, (255, 255, 255), (x, 0), (x, self.size[1] * self.cell_size))
        for y in range(0, self.size[1] * self.cell_size, self.cell_size):
            pygame.draw.line(screen, (255, 255, 255), (0, y), (self.size[0] * self.cell_size, y))

    def draw_snake(self, screen, snake):
        for segment in snake.position:
            pygame.draw.rect(screen, (0, 255, 0), (segment[0] * self.cell_size, segment[1] * self.cell_size, self.cell_size, self.cell_size))

    def draw_circle(self, screen, circle):
        pygame.draw.circle(screen, (255, 0, 0), (circle.position[0] * self.cell_size + self.cell_size // 2, circle.position[1] * self.cell_size + self.cell_size // 2), self.cell_size // 2)
