import pygame
from pygame import font
from typing import Tuple
pygame.init()
class ScoreCounter:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)  # Adjust the font size here
        self.score_multiplier = 0

    def increase_score(self):
        self.score += 5
        self.score += 2 * self.score_multiplier

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    def get_circles_eaten(self, n):
        self.score_multiplier = n
