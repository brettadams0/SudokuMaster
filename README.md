# SudokuMaster

SudokuMaster is a command-line tool that allows users to either solve a Sudoku puzzle or generate a new one. It supports different difficulty levels for puzzle generation, making it suitable for both beginners and advanced players. This project is designed to provide a seamless Sudoku-solving experience while allowing users to generate and solve puzzles directly from their terminal.

## Features
- **Sudoku Solver**: Input a Sudoku puzzle, and the program will solve it instantly.
- **Sudoku Generator**: Generate new Sudoku puzzles with varying difficulty levels (Easy, Medium, Hard).
- **Interactive CLI**: The user-friendly command-line interface guides you through the process of solving or generating puzzles.
- **Continuous Operation**: After completing each task, the program prompts the user for the next action, ensuring a smooth workflow.

## Getting Started

### Prerequisites
- Python 3.6 or later

### Installation
1. Clone this repository:
```bash
git clone https://github.com/brettadams0/SudokuMaster.git
```
Navigate to the project directory:
```bash
cd SudokuMaster
```
Usage
Run the program:

```bash
python app.py
```
Follow the prompts to solve a puzzle, generate a new one, or quit the program.

Example
```bash
Welcome to Sudoku Solver & Generator
Choose: [S]olve a puzzle, [G]enerate a new one, or [Q]uit: G
Choose difficulty: [E]asy, [M]edium, [H]ard: M

Generated Sudoku (medium):
5 3 .  | . 7 .  | . . .
6 . .  | 1 9 5  | . . .
. 9 8  | . . .  | . 6 .
- - - - - - - - - - -
8 . .  | . 6 .  | . . 3
4 . .  | 8 . 3  | . . 1
7 . .  | . 2 .  | . . 6
- - - - - - - - - - -
. 6 .  | . . .  | 2 8 .
. . .  | 4 1 9  | . . 5
. . .  | . 8 .  | . 7 9

Would you like to solve this Sudoku? [Y/N]: Y

Solved Sudoku:
5 3 4  | 6 7 8  | 9 1 2
6 7 2  | 1 9 5  | 3 4 8
1 9 8  | 3 4 2  | 5 6 7
- - - - - - - - - - -
8 5 9  | 7 6 1  | 4 2 3
4 2 6  | 8 5 3  | 7 9 1
7 1 3  | 9 2 4  | 8 5 6
- - - - - - - - - - -
9 6 1  | 5 3 7  | 2 8 4
2 8 7  | 4 1 9  | 6 3 5
3 4 5  | 2 8 6  | 1 7 9
```

## Contributing
Feel free to open an issue or submit a pull request if you'd like to contribute to the project.
