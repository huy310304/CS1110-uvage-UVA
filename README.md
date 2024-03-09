# Final Project - CS 1110 @ UVA-CS

This project is a part of the coursework for CS 1110 at the University of Virginia. For more course details, visit the [Course Site and Information](https://www.coursicle.com/virginia/courses/CS/1110/).

## Overview

This README provides details on our Flappy Bird game project, originally developed using the `uvage` library for the CS1110 course. Due to the `uvage` library's limited availability outside the course, we are transitioning this game to Pygame for broader access and playability.

## Demo

*Demo details or link to video will be added soon.*

## How To Download and Play Pygame Version

We've successfully converted this game to Pygame to make it accessible to a wider audience. The Pygame version maintains the core gameplay while enhancing both accessibility and playability.

Follow these specific steps to download and run the game on your local computer:

1. **Install Python**: Ensure Python is installed on your system. If it's not already installed, you can download and install it from [python.org](https://www.python.org/).

2. **Install Pygame**: Open your terminal (Command Prompt on Windows, Terminal on macOS and Linux) and install Pygame by executing the following command:
    ```
    pip install pygame
    ```

3. **Download the Game**: Clone the game repository from GitHub to your local machine using the following command in your terminal:
    ```
    git clone https://github.com/huy310304/flappy-bird-game.git
    ```
   This command creates a local copy of the game source code on your computer.

4. **Run the Game**: Navigate to the directory containing the game's Pygame version. You can do this by typing:
    ```
    cd flappy-bird-game/pygame
    ```
   Once you're in the correct directory, start the game by running:
    ```
    python game.py
    ```
   This will launch the game window, and you can start playing the Pygame version of Flappy Bird right away.

Remember, the commands `python game.py` might vary depending on your Python installation. If you have Python 3 installed alongside Python 2, you may need to use `python3 game.py` instead.


## How to Play (uvage version for CS_1110)

### Starting the Game

- Launch the game script in your Python environment.
- Press **ENTER** to begin Level 1.

### Controls

- **Space** or **Up Arrow**: Flap the bird upwards. Release to let it fall.
- **R**: Restart the game after a game over.
- **N**: Advance to the next level after completing Level 1.

### Objectives

- Guide the bird through gaps between pipes without colliding.
- Aim to cross as many pipes as possible to increase your score.

### Levels

- **Level 1**: Features standard gameplay with static pipes.
- **Level 2**: Introduces moving pipes, adding an extra layer of challenge.

### Game Over

- The game concludes when the bird collides with pipes or the ground.
- Each collision reduces the health bar until the game ends.

### Winning the Game

- Successfully navigate through 20 pipes to complete a level.
- Completing Level 1 allows progression to Level 2 by pressing **N**.

## Features

- Animated sprite for the bird character.
- Dynamic pipe movement in Level 2, with vertical motion.
- Score tracking through invisible lines.
- A health bar that depletes upon collision.
- Options to restart or progress levels.

## Credits

Developed by Huy Nguyen and Theodore LengKong as a collaborative final project for the CS1110 course, initially using the `uvage` library. The transition to Pygame aims to extend the game's reach beyond the confines of the UVA CS 1110 course.

Enjoy :D
