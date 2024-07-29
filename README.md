# Classic Snake

## Overview

This is a classic Snake game implemented using Python and the Turtle graphics library. The game features a snake that moves around the screen, eats food, and grows longer with each meal. The goal is to achieve the highest score possible before the snake collides with the wall or itself.

## Author

- **NightFox**

## Timestamp

- **2024-07-29** (Timestamp: 1722258268.1120665)


## Features

- **Basic Gameplay**: Control the snake to eat food and grow.
- **Scoreboard**: Displays the current score in the top right corner.
- **Grid**: A grid is drawn on the screen to help visualize movement and collisions.
- **Dynamic Food Generation**: Food appears at random positions on the grid.

## Installation

To run this game, you need Python and the Turtle graphics library. The Turtle module comes pre-installed with Python, so no additional installation is required for the library.

1. **Install Python**: Make sure Python 3.x is installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone or download the repository containing the `snake_game.py` file.

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

3. **Run the Game**: Execute the game script using Python.

    ```sh
    python snake_game.py
    ```

## Controls

- **Arrow Keys**:
  - **Up Arrow**: Move the snake up.
  - **Down Arrow**: Move the snake down.
  - **Left Arrow**: Move the snake left.
  - **Right Arrow**: Move the snake right.

## Gameplay

- **Objective**: Eat the food items that appear on the screen to grow the snake and increase your score.
- **Game Over**: The game ends if the snake collides with the wall or itself.
- **Score**: The score increases by 1 each time the snake eats a food item.

## Code Description

- **`Snake` Class**: Contains all game logic, including snake movement, food generation, and collision detection.
  - **`__init__`**: Initializes the game screen, snake, scoreboard, and controls.
  - **`setup_screen`**: Configures the game window.
  - **`draw_grid`**: Draws a grid on the screen for better gameplay visualization.
  - **`create_snake`**: Creates and initializes the snake.
  - **`set_colors`**: Sets colors for each segment of the snake.
  - **`setup_controls`**: Maps keyboard controls to snake movement.
  - **`create_scoreboard`**: Displays the score on the screen.
  - **`update_scoreboard`**: Updates the displayed score.
  - **`add_food`**: Adds food items at random locations.
  - **`move_snake`**: Moves the snake and checks for collisions.
  - **`turn_left`, `turn_right`, `turn_up`, `turn_down`**: Change the direction of the snake.
  - **`check_food_collision`**: Checks if the snake has eaten food.
  - **`add_body`**: Adds a new segment to the snake's body.
  - **`run`**: Main game loop that handles the game's progression.

## License

This project is licensed under the [GPL-3.0 License](https://opensource.org/licenses/GPL-3.0). See the [LICENSE](LICENSE) file for details.


## Acknowledgments

- Python and the Turtle graphics library for providing a simple way to create graphical applications.
- Classic Snake game inspiration for game mechanics and design.

---

Feel free to modify and extend this game to add more features and improve the gameplay experience!
