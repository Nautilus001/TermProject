# To run
1. Clone project to your machine
2. Navigate to the directory in terminal
3. Run "pip install -r requirements.txt"
4. Run "python game.py"


# Testing Breakdown
1. Slash
2. Coverage
3. Mutation
4. Mocking

The core classes, functions, and methods are as follows:

1. Game: This class will handle the main game loop and manage the game state.
   - `__init__()`: Initializes the game state.
   - `run()`: Starts the game loop.
   - `handle_events()`: Handles user input events.
   - `update()`: Updates the game state.
   - `draw()`: Renders the game on the screen.

2. Snake: This class represents the snake in the game.
   - `__init__()`: Initializes the snake's position, length, and direction.
   - `move()`: Moves the snake in the current direction.
   - `change_direction()`: Changes the direction of the snake based on user input.
   - `check_collision()`: Checks for collisions with walls or the snake's own body.
   - `grow()`: Increases the length of the snake when it collides with a circle.

3. Circle: This class represents the circle that appears randomly on the grid.
   - `__init__()`: Initializes the circle's position.
   - `generate_new_position()`: Generates a new random position for the circle on the grid.

4. Grid: This class represents the game grid.
   - `__init__()`: Initializes the grid with the specified size.
   - `draw()`: Renders the grid on the screen.
   - `draw_snake()`: Renders the snake on the grid.
   - `draw_circle()`: Renders the circle on the grid.

5. ScoreCounter: This class manages the player's score.
   - `__init__()`: Initializes the score counter.
   - `increase_score()`: Increases the score based on the number of circles collected.
