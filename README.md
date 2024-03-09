# Final Project - CS 1110 @ UVA

This project is a part of the coursework for CS 1110 at the University of Virginia. For more course details, visit the [Course Site and Information](https://www.coursicle.com/virginia/courses/CS/1110/).

## Overview

This README provides details on our Flappy Bird game project, originally developed using the `uvage` library for the CS1110 course. Due to the `uvage` library's limited availability outside the course, we are transitioning this game to Pygame for broader access and playability.

## Demo

*Demo details or link to video will be added soon.*

## How To Download and Play Pygame Version

I have finished converting this game to Pygame to make it accessible to a wider audience. The Pygame version will maintain the core gameplay while enhancing accessibility and playability.

To run the game on your local computer, follow these specific steps:

1. **Install Python**: Make sure Python is installed on your system. If not, download and install it from [python.org](https://www.python.org/).
2. **Install Pygame**: Open your terminal and install Pygame by running: `pip install pygame`
3. **Download the game**: Clone the repository using `git clone https://github.com/huy310304/flappy-bird-game.git`
4. **Run the game**: Navigate to the pygame folder using `cd flappy-bird-game/pygame` and run the game by `python game.py`.

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
