🐦 Flappy Bird Game Using Python

1. Introduction

Flappy Bird is a simple 2D game developed using Python and the Pygame library.

In this game, the player controls a bird that flies through gaps between pipes. The bird moves upward when the SPACE key is pressed and falls downward due to gravity.

The main objective is to avoid obstacles and score as many points as possible.

This project also includes four built-in test cases to verify the functionality of the game.

2. Project Objectives

To understand Python programming.

To learn basic game development using Pygame.

To implement bird movement using gravity and velocity.

To understand collision detection.

To implement a scoring system.

To execute test cases and verify program functionality.

3. Technologies Used

Technology

Purpose

Python

Programming language

Pygame

Game development library

Random

Generate random pipe positions

Sys

Exit the game

Argparse

Handle command-line arguments

4. Features

Simple and attractive game interface.

Bird movement and jumping physics.

Gravity simulation.

Random pipe generation.

Collision detection.

Automatic score calculation.

Game Over screen.

Restart game functionality.

Four built-in test cases.

Separate game and testing modes.

5. Project Structure

Flappy-Bird/
│
├── flappy_bird.py
├── README.md
└── requirements.txt

6. Installation and Setup

Step 1: Install Python

Download Python from:

https://www.python.org/downloads/

Step 2: Install Pygame

Open the terminal and execute:

pip install pygame

Step 3: Create Project Folder

mkdir Flappy-Bird
cd Flappy-Bird

Save your Python code as:

flappy_bird.py

Step 4: Create requirements.txt

Add the following line:

pygame

7. How to Run the Game

Open the terminal in your project folder and execute:

python flappy_bird.py

The Flappy Bird game window will open.

8. Game Controls

Key

Function

SPACE

Make the bird jump

SPACE after Game Over

Restart the game

Window Close Button

Exit the game

9. Testing the Project

This project contains four test cases to check the game functionality.

To run all test cases, execute:

python flappy_bird.py --test

Test Case 1: Normal Input

Purpose: To check the normal movement of the bird under gravity.

Input:

Initial position = 300

Initial velocity = 0

Expected Output:

Frame 1: velocity=1, y=301
Frame 2: velocity=2, y=303
Test Case 1: PASSED

Test Case 2: Boundary Input

Purpose: To check whether the bird collides with the top boundary or ground.

Expected Output:

Ground Collision: Game Over
Velocity=-9, y=-4
Bird left the top: Game Over
Test Case 2: PASSED

Test Case 3: Invalid Input

Purpose: To verify that an input other than SPACE does not trigger a jump.

Expected Output:

Key ignored: velocity=1, y=301
Test Case 3: PASSED

Test Case 4: Different Valid Scenario

Purpose: To check bird jumping and pipe scoring functionality.

Expected Output:

Velocity=-9, y=291
Pipe passed! Score: 1
Test Case 4: PASSED

Final Testing Result

===== FLAPPY BIRD TEST CASES =====

TEST CASE 1: Normal Input
Test Case 1: PASSED

TEST CASE 2: Boundary Input
Test Case 2: PASSED

TEST CASE 3: Invalid Input
Test Case 3: PASSED

TEST CASE 4: Different Valid Scenario
Test Case 4: PASSED

ALL TEST CASES PASSED!

10. Working Principle

Bird Physics

Gravity continuously pulls the bird downward. Pressing SPACE applies upward velocity.

Collision Detection

The program checks whether the bird touches the top boundary, ground, or pipes.

Pipe Generation

Pipes are generated at random positions with a fixed gap between them.

Scoring System

The player receives one point whenever the bird successfully passes a pipe.

Game Over

When the bird collides with an obstacle or boundary, the game ends.

11. Learning Outcomes

After completing this project, we learn:

Python functions and variables.

Conditional statements and loops.

Lists and dictionaries.

Random number generation.

Pygame graphics and event handling.

Game physics and collision detection.

Command-line argument handling.

Basic software testing.

12. Future Enhancements

Add sound effects.

Add background music.

Add a high-score system.

Improve bird and pipe graphics.

Add multiple difficulty levels.

Add more test cases.

13. Conclusion

The Flappy Bird project demonstrates the basic concepts of Python programming and game development using Pygame.

It also demonstrates how test cases can be used to verify different functions of a program. All four built-in test cases are designed to pass with the given code.

This project is useful for beginners who want to learn Python programming and basic software testing.

14. Author

Project Name: Flappy Bird Game

Programming Language: Python

Library: Pygame

Project Type: Python Game Development

Purpose: Educational Project

⭐ If you like this project, you can star the repository on GitHub!