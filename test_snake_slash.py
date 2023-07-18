from slash import slash
from snake import Snake

@slash.fixture
def snake():
    # Create a Snake object with a small grid size for testing
    return Snake(grid_size=(5, 5))

@slash.parametrize('direction', ['UP', 'DOWN', 'LEFT', 'RIGHT'])
def test_initial_direction(snake, direction):
    assert snake.direction == 'UP'

@slash.parametrize('direction, expected_direction', [
    ('UP', 'UP'),
    ('DOWN', 'DOWN'),
    ('LEFT', 'LEFT'),
    ('RIGHT', 'RIGHT'),
    ('INVALID', 'UP'),  # Invalid direction should not change the current direction
])
def test_change_direction(snake, direction, expected_direction):
    snake.change_direction(direction)
    assert snake.direction == expected_direction

@slash.parametrize('initial_position, new_direction, expected_position', [
    ([(2, 2)], 'UP', [(2, 1)]),
    ([(2, 2)], 'DOWN', [(2, 3)]),
    ([(2, 2)], 'LEFT', [(1, 2)]),
    ([(2, 2)], 'RIGHT', [(3, 2)]),
])
def test_move(snake, initial_position, new_direction, expected_position):
    snake.position = initial_position
    snake.direction = new_direction
    snake.move()
    assert snake.position == expected_position

@slash.parametrize('initial_position, new_direction, should_collide', [
    ([(0, 0)], 'UP', True),    # Collision with top boundary
    ([(4, 4)], 'RIGHT', True), # Collision with right boundary
    ([(2, 0)], 'UP', True),    # Collision with top boundary
    ([(2, 2), (2, 1)], 'UP', True), # Self-collision
    ([(2, 2), (2, 1), (2, 0)], 'UP', True), # Self-collision
    ([(2, 2), (2, 1), (2, 0)], 'LEFT', False), # No collision
])
def test_check_collision(snake, initial_position, new_direction, should_collide):
    snake.position = initial_position
    snake.direction = new_direction
    assert snake.check_collision(grid_size=(5, 5)) == should_collide

@slash.parametrize('position, should_collide', [
    ((2, 2), True),   # Collides with the snake's head
    ((1, 1), False),  # No collision with the snake's head
])
def test_collides_with(snake, position, should_collide):
    snake.position = [(2, 2), (2, 1), (1, 1)]
    assert snake.collides_with(position) == should_collide

@slash.parametrize('initial_position, expected_grown_position', [
    ([(2, 2)], [(2, 2), (2, 2)]),
    ([(4, 4), (4, 3)], [(4, 4), (4, 3), (4, 3)]),
])
def test_grow(snake, initial_position, expected_grown_position):
    snake.position = initial_position
    snake.grow()
    assert snake.position == expected_grown_position

if __name__ == '__main__':
    slash.main()
