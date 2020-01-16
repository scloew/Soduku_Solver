from .cell import Cell
from .group import Group


class Puzzle:

    def __init__(self, puzzle_file):
        with open(puzzle_file, 'r') as in_file:
            self.puzzle = in_file.readlines() #TODO need to conver this to into cells at some point...
        self.cells = []
        for line in self.puzzle:
            temp_cells = []
            for v in line:
                if v != '\n':
                    temp_cells.append(Cell(int(v)))
            self.cells.append(temp_cells)

    def print_puzzle(self) :
        for index, line in enumerate(self.puzzle):
            temp_line = '|'.join(a + b + c for a, b, c in zip(line[::3], line[1::3], line[2::3]))
            print(' '.join(temp_line))
            if index in {2, 5}:
                print('-  ' * 8)
