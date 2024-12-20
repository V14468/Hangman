This project implements the classic Hangman Game, developed entirely in the C programming language. The game offers a fun and interactive experience, challenging players to guess words from various categories while managing a limited number of attempts. The implementation features modular design, clean logic, and customizable elements, making it an excellent educational resource and entertaining game. The game is played in a console environment, showcasing the power of C to create engaging applications without requiring a graphical interface.

Features
1. Category Selection
Players can choose from five distinct categories:
Movies/Series: Famous movies and TV series titles.
Sports: Popular sports and team names, including IPL and Premier League teams.
Famous Personalities: Renowned historical figures, athletes, scientists, and celebrities.
Places: Cities, landmarks, and globally significant locations.
People from Our Class: A customizable list of names for a personalized touch.

2. Randomized Word Selection
Each time the game starts, a random word is selected from the chosen category, ensuring replayability and unpredictability.

3. Hints System
Hints corresponding to each word are displayed when the player is left with only three attempts, providing an extra layer of support without making the game too easy.

4. Attempts and Feedback
Players are allowed a maximum of 9 incorrect guesses. After each guess, feedback is provided, indicating whether the guess was correct or not.

5. Graphical ASCII Art
The game displays a graphical representation of the hangman as the player progresses. This simple yet effective visual feedback enhances the gaming experience.

6. Replay Option
Once the game ends, players are prompted to decide whether they want to play again, allowing for multiple rounds of fun without restarting the program.

How It Works
1. Game Flow
The game begins with a prompt asking the player to select a category.
A random word from the chosen category is selected, and the player must guess letters to complete the word.
If the player guesses the word correctly before running out of attempts, they win. Otherwise, they lose, and the word is revealed.
2. Key Functionalities
Word Display: Shows the word with guessed letters revealed and remaining letters hidden as underscores (_).
Letter Guessing: Players enter one letter at a time to attempt to reveal the hidden word.
Hint Display: A hint related to the word is shown after a certain number of incorrect guesses.
Attempts Tracking: The game tracks the number of incorrect guesses and reduces the remaining attempts accordingly.
ASCII Art Hangman: A graphical representation of the hangman changes with each incorrect guess.

Code Details
1. Preprocessor Directives
#include <stdio.h>: Used for input and output operations.
#include <stdlib.h>: Used for memory allocation and random number generation.
#include <string.h>: Used for string manipulation.
#include <time.h>: Used for seeding the random number generator.
#include <ctype.h>: Used for character handling, such as case conversion.
2. Core Logic
Dynamic Word Selection
Words and hints are stored in arrays of strings (pointer arrays).
A random index is generated using rand() to pick a word and its corresponding hint.
Functions
void display(char word[], int guessed[]): Displays the word with guessed letters revealed and remaining letters as underscores.
int wordG(int guessed[], int length): Checks if the entire word has been guessed.
void draw(int left): Displays the hangman using ASCII art based on the number of remaining attempts.
Game Variables
char **words: Points to the selected word list.
char **hints: Points to the corresponding hints list.
int guessed[]: Tracks the guessed status of each letter in the selected word.
