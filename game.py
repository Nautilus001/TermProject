import pygame
from snake import Snake
from circle import Circle
from grid import Grid
from score_counter import ScoreCounter

class Game:
    def __init__(self):
        self.grid_size = (10, 10)
        self.grid = Grid(self.grid_size)
        self.snake = Snake(self.grid_size)
        self.circle = Circle(self.grid_size)
        self.score_counter = ScoreCounter()
        self.circles_eaten = 0
        self.paused = False
        self.running = True

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(self.grid.get_screen_size())
        pygame.display.set_caption("Snake Game")
        self.paused = False
        self.running = True
        while self.running:
            clock.tick(5)  # Adjust the speed of the game here
            self.handle_events()
            while self.paused:
                self.is_paused()
            self.update()
            self.draw(screen)

            pygame.display.flip()

        pygame.quit()

    def is_paused(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                    break
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.snake.change_direction("UP")
                elif event.key == pygame.K_s:
                    self.snake.change_direction("DOWN")
                elif event.key == pygame.K_a:
                    self.snake.change_direction("LEFT")
                elif event.key == pygame.K_d:
                    self.snake.change_direction("RIGHT")
                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                    break
                elif event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        self.snake.move()

        if self.snake.check_collision(self.grid_size):
            self.game_over()

        if self.snake.collides_with(self.circle.position):
            self.circle.pop
            self.snake.grow()
            self.circles_eaten += 1
            self.circle = Circle(self.grid_size)
            self.score_counter.get_circles_eaten(self.circles_eaten)

        self.score_counter.increase_score()

    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.grid.draw(screen)
        self.grid.draw_snake(screen, self.snake)
        self.grid.draw_circle(screen, self.circle)
        self.score_counter.draw(screen)

    def game_over(self):
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
