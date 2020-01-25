from .cell import Cell
from .group import Group


class Puzzle:

    def __init__(self, puzzle_file):
        self.cells = []
        with open(puzzle_file, 'r') as in_file:
            self.cells = [[Cell(v) for v in line if v != '\n'] for line in in_file.readlines()]
        self.update_number = sum(1 for i in range(9) for j in range(9) if self.cells[i][j].val == '0')
        self._build_column_groups()
        self._build_row_groups()
        self._build_square_groups()

    def solve_puzzle(self):
        """
        iterate through groups updating cells; when cell takes value, updata groups
        do while puzzle not solved. Will need to update process for handling guessing
        """
        debug_count = 1
        while self.update_number != 0: #TODO doesn't handle guessing; or invalid puzzle
            debug_count += 1
            for row_num in range(9):
                for col_num in range(9):
                    current_cell = self.cells[row_num][col_num]
                    did_update = current_cell.update_options(self.rows[row_num])
                    did_update = did_update or current_cell.update_options(self.columns[col_num])
                    did_update = did_update or current_cell.update_options(self._square_dict[(int(row_num / 3), int(col_num / 3))])
                    if did_update:
                        self.update_number -= 1
                        self.rows[row_num].update_options(current_cell.val)
                        self.columns[col_num].update_options(current_cell.val)
                        self._square_dict[(int(row_num / 3), int(col_num / 3))].update_options(current_cell.val)
            if debug_count > 500:
                print('timeout')
                return False


    def _build_column_groups(self):
        self.columns = [Group([self.cells[j][i] for j in range(9)]) for i in range(9)]

    def _build_row_groups(self):
        self.rows = [Group(self.cells[i]) for i in range(9)]

    def _build_square_groups(self):
        self.squares = []
        self._square_dict = {}
        for off_set in range(3):
            row_offset = 0
            for x_index in range(0, 9, 3):
                temp_list = []
                for y_index in range(0, 3):
                    temp_list += self.cells[y_index+3*off_set][x_index:x_index + 3]
                self.squares.append(Group(temp_list)) #TODO nice list comprhension for this?
                self._square_dict.update({(off_set, row_offset):self.squares[-1]})
                row_offset += 1

    def print_puzzle(self):
        for index, row in enumerate(self.cells):
            temp_str = ''.join([c.val for c in row])
            temp_line = '|'.join(a + b + c for a, b, c in zip(temp_str[::3], temp_str[1::3], temp_str[2::3]))
            print(' '.join(temp_line))
            if index in {2, 5}:
                print('-  ' * 8)
