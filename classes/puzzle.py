from .cell import Cell
from .group import Group


class Puzzle:

    def __init__(self, puzzle_file):
        self.cells = []
        with open(puzzle_file, 'r') as in_file:
            self.cells = [[Cell(v) for v in line if v != '\n'] for line in in_file.readlines()]
        self._build_column_groups()
        self._build_row_groups()
        self._build_square_group()

    def solve_puzzle(self):
        """
        iterate through groups updating cells; when cell takes value, updata groups
        do while puzzle not solved. Will need to update process for handling guessing
        """
        raise NotImplementedError #TODO implement solving algorithm

    def _build_column_groups(self):
        self.columns = [Group([self.cells[j][i] for j in range(9)]) for i in range(9)]

    def _build_row_groups(self):
        self.rows = [Group(self.cells[i]) for i in range(9)]

    def _build_square_group(self):
        self.squares = []
        for off_set in range(3):
            for x_index in range(0, 9, 3):
                temp_list = []
                for y_index in range(0, 3):
                    temp_list += self.cells[y_index+3*off_set][x_index:x_index + 3]
                self.squares.append(Group(temp_list)) #TODO nice list comprhension for this?

    def print_puzzle(self):
        for index, row in enumerate(self.cells):
            temp_str = ''.join([c.val for c in row])
            temp_line = '|'.join(a + b + c for a, b, c in zip(temp_str[::3], temp_str[1::3], temp_str[2::3]))
            print(' '.join(temp_line))
            if index in {2, 5}:
                print('-  ' * 8)
