import unittest
import pygame
from game import Game

# Mock the Pygame functions to avoid initializing the display during testing
pygame.init = lambda: None
pygame.quit = lambda: None
pygame.time.Clock = lambda: None
pygame.time.Clock.tick = lambda x: None
pygame.display.set_mode = lambda x: None
pygame.display.set_caption = lambda x: None
pygame.event.get = lambda: []

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_snake_initial_position(self):
        grid_size = self.game.grid_size
        self.assertEqual(self.game.snake.position, [(grid_size[0] // 2, grid_size[1] // 2)])

    def test_snake_initial_direction(self):
        self.assertEqual(self.game.snake.direction, "RIGHT")

    def test_snake_move(self):
        grid_size = self.game.grid_size
        self.game.snake.move()
        self.assertEqual(self.game.snake.position, [((grid_size[0] // 2) + 1, grid_size[1] // 2)])

    def test_snake_change_direction(self):
        self.game.snake.change_direction("DOWN")
        self.assertEqual(self.game.snake.direction, "DOWN")

    def test_snake_collision(self):
        self.game.snake.position = [(0, 0), (1, 0), (2, 0)]  # Create a collision scenario
        self.game.snake.move()
        self.assertTrue(self.game.snake.check_collision(self.game.grid_size))

    def test_snake_no_collision(self):
        self.assertFalse(self.game.snake.check_collision(self.game.grid_size))

    def test_circle_eaten(self):
        initial_score = self.game.score_counter.score
        self.game.snake.position = [(0, 0), self.game.circle.position]  # Place snake head on the circle
        self.game.update()
        self.assertEqual(self.game.score_counter.score, initial_score + 5 + (2*self.game.score_counter.score_multiplier))
        self.assertEqual(len(self.game.snake.position), 2)

if __name__ == "__main__":
    unittest.main()
