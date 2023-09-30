# Snake Game User Manual

Welcome to the Snake Game! This user manual will guide you through the installation process and explain how to play the game.

## Table of Contents
1. [Installation](#installation)
2. [Game Controls](#game-controls)
3. [Gameplay](#gameplay)
4. [Scoring](#scoring)
5. [Game Over](#game-over)

## 1. Installation <a name="installation"></a>

To play the Snake Game, you need to have Python and the Tkinter library installed on your machine. Follow the steps below to install the required dependencies:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have downloaded the Snake Game files.
3. Run the following command to install the required dependencies:

```
pip install -r requirements.txt
```

Once the installation is complete, you are ready to play the game!

## 2. Game Controls <a name="game-controls"></a>

The Snake Game can be controlled using the arrow keys on your keyboard. The controls are as follows:

- Up Arrow: Move the snake upwards.
- Down Arrow: Move the snake downwards.
- Left Arrow: Move the snake to the left.
- Right Arrow: Move the snake to the right.

## 3. Gameplay <a name="gameplay"></a>

The objective of the Snake Game is to control the snake and eat the food to grow longer. As the snake eats the food, its length increases, making it more challenging to navigate without colliding with the walls or its own body.

To start the game, run the following command in the terminal or command prompt:

```
python main.py
```

The game window will open, and you will see a black canvas representing the game area. The snake and food will appear on the canvas.

Use the arrow keys to control the snake's movement. The snake will continuously move in the direction you choose until you change its direction or it collides with the walls or its own body.

## 4. Scoring <a name="scoring"></a>

Each time the snake eats the food, your score will increase by one. The score is displayed at the top of the game window.

## 5. Game Over <a name="game-over"></a>

The game ends when the snake collides with the walls or its own body. When the game is over, a "Game Over" message will be displayed on the canvas.

To play again, close the game window and run the `python main.py` command again.

Enjoy playing the Snake Game!