# Snake Game

This is a Python code that implements the Snake game using the Pygame library. The game involves controlling a snake that moves around the screen in search of apples. Each time the snake eats an apple, its size increases and the player earns points. The goal is to make the snake grow as long as possible without colliding with the screen boundaries or itself.

## Requirements

- Python 3.x
- Pygame

## Installing
1. Install the Pygame library by running the following command in the terminal:
```bash
pip3 install pygame
```
2. Download the game source code and save it on your computer.
3. Open a terminal and navigate to the directory where you saved the game file.
4. Run the following command to start the game:
```bash
python snake_game.py
```
6. Use the arrow keys to control the direction of the snake (up, down, left, and right).
7. Try to collect as many apples as possible without colliding with the boundaries or the snake itself.
8. When the game ends, the "Game Over!" message will be displayed on the screen for a few seconds before closing the game.

## Customizations

You can customize the game by adjusting the following variables in the code:

- `resolution`: sets the resolution of the game window.
- `square_size`: sets the size of the board squares.
- `snake_skin`: sets the size of the snake.
- `apple`: sets the size of the apple.
- `fps_controller.tick()`: sets the frames per second rate of the game.
