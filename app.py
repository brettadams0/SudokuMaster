import random
import numpy as np

class SudokuSolver:
    def __init__(self, grid):
        self.grid = np.array(grid)
        self.size = 9
        self.subgrid_size = 3

    def is_valid(self, num, row, col):
        # Check if num is not in the current row and column
        for i in range(self.size):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
        # Check if num is not in the current subgrid
        start_row, start_col = row - row % self.subgrid_size, col - col % self.subgrid_size
        for i in range(self.subgrid_size):
            for j in range(self.subgrid_size):
                if self.grid[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve(self):
        empty = self.find_empty_location()
        if not empty:
            return True  # Solved
        row, col = empty
        for num in range(1, 10):
            if self.is_valid(num, row, col):
                self.grid[row][col] = num
                if self.solve():
                    return True
                self.grid[row][col] = 0  # Reset on backtrack
        return False

    def find_empty_location(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    return i, j
        return None

    def print_grid(self):
        for i in range(self.size):
            if i % 3 == 0 and i != 0:
                print("- " * 11)
            for j in range(self.size):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                print(self.grid[i][j] if self.grid[i][j] != 0 else ".", end=" ")
            print()

class SudokuGenerator:
    def __init__(self, difficulty='medium'):
        self.difficulty = difficulty
        self.size = 9

    def generate(self):
        grid = [[0] * self.size for _ in range(self.size)]
        self.fill_grid(grid)  # Fill the grid completely
        num_clues = self.get_clue_count()
        self.remove_numbers(grid, num_clues)
        return grid

    def fill_grid(self, grid):
        """Fill the grid using a randomized backtracking algorithm to generate a full Sudoku."""
        numbers = list(range(1, 10))
        for i in range(self.size):
            for j in range(self.size):
                if grid[i][j] == 0:
                    random.shuffle(numbers)
                    for num in numbers:
                        if self.is_valid(grid, num, i, j):
                            grid[i][j] = num
                            if self.fill_grid(grid):
                                return True
                            grid[i][j] = 0
                    return False
        return True

    def is_valid(self, grid, num, row, col):
        """Check if placing num in grid[row][col] is valid."""
        for i in range(self.size):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + start_row][j + start_col] == num:
                    return False
        return True

    def get_clue_count(self):
        return {
            'easy': 36,
            'medium': 27,
            'hard': 17,
        }.get(self.difficulty, 27)

    def remove_numbers(self, grid, num_clues):
        """Remove numbers from the filled grid to create the puzzle."""
        cells = [(i, j) for i in range(self.size) for j in range(self.size)]
        random.shuffle(cells)
        for _ in range(self.size * self.size - num_clues):
            row, col = cells.pop()
            grid[row][col] = 0

    def print_grid(self, grid):
        for i in range(self.size):
            if i % 3 == 0 and i != 0:
                print("- " * 11)
            for j in range(self.size):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
            print()

if __name__ == "__main__":
    while True:
        print("Welcome to Sudoku Solver & Generator")
        choice = input("Choose: [S]olve a puzzle, [G]enerate a new one, or [Q]uit: ").strip().upper()

        if choice == 'S':
            grid = [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
            ]
            solver = SudokuSolver(grid)
            print("\nSudoku to Solve:")
            solver.print_grid()
            if solver.solve():
                print("\nSolved Sudoku:")
                solver.print_grid()
            else:
                print("No solution exists.")

        elif choice == 'G':
            difficulty = input("Choose difficulty: [E]asy, [M]edium, [H]ard: ").strip().upper()
            difficulty_map = {'E': 'easy', 'M': 'medium', 'H': 'hard'}
            generator = SudokuGenerator(difficulty=difficulty_map.get(difficulty, 'medium'))
            grid = generator.generate()
            print(f"\nGenerated Sudoku ({difficulty_map.get(difficulty, 'medium')}):")
            generator.print_grid(grid)
            if input("Would you like to solve this Sudoku? [Y/N]: ").strip().upper() == 'Y':
                solver = SudokuSolver(grid)
                if solver.solve():
                    print("\nSolved Sudoku:")
                    solver.print_grid()
                else:
                    print("No solution exists.")

        elif choice == 'Q':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
