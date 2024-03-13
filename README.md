# Final Project - CS 1110 @ UVA-CS

This project is a part of the coursework for CS 1110 at the University of Virginia. For more course details, visit the [Course Site and Information](https://www.coursicle.com/virginia/courses/CS/1110/).

## Overview

This README provides details on our Flappy Bird game project, originally developed using the `uvage` library for the CS1110 course. Due to the `uvage` library's limited availability outside the course, I have transitioned this game to using `pygame` for broader access and playability.

## Demo (PYGAME VERSION)

![Gameplay Demo](demo.gif)

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

5. **Play the Game**: The `pygame` version encompasses most of the fundamental features in the `uvage` version described below. To interact with the game, simply press either the SPACE key or the UP ARROW key to make the bird flap upwards.

## Features (UVAGE Version)

- Animated sprite for the bird character.
- Dynamic pipe movement in Level 2, with vertical motion.
- Score tracking through invisible lines.
- A health bar that depletes upon collision.
- Options to restart or progress levels.

## Credits

Developed by Huy Nguyen and Theodore LengKong as a collaborative final project for the CS1110 course, initially using the `uvage` library. The transition to Pygame aims to extend the game's reach beyond the confines of the UVA CS 1110 course.

Enjoy :D
