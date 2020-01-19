from .cell import Cell
from .group import Group


class Puzzle:

    def __init__(self, puzzle_file):
        self.cells = []
        with open(puzzle_file, 'r') as in_file:
            self.cells = [[Cell(v) for v in line if v != '\n'] for line in in_file.readlines()]
        self._build_column_groups()

    def _build_column_groups(self):
        self.columns = [Group([self.cells[i][j] for j in range(9)]) for i in range(9)]

    def _build_row_groups(self):
        self.rows = [Group(self.cells[i]) for i in range(9)]

    def _build_square_group(self):
        raise NotImplementedError #to do implement this

    def print_puzzle(self):
        for index, row in enumerate(self.cells):
            temp_str = ''.join([c.val for c in row])
            temp_line = '|'.join(a + b + c for a, b, c in zip(temp_str[::3], temp_str[1::3], temp_str[2::3]))
            print(' '.join(temp_line))
            if index in {2, 5}:
                print('-  ' * 8)
