from .cell import Cell
from .group import Group
from ._contants import cell_status


class Puzzle:

    def __init__(self, puzzle_file):
        self.cells = []
        with open(puzzle_file, 'r') as in_file:
            self.cells = [[Cell(v) for v in line if v != '\n'] for line in in_file.readlines()]
        self.update_number = sum(1 for i in range(9) for j in range(9) if self.cells[i][j].val == '0')
        self._build_column_groups()
        self._build_row_groups()
        self._build_square_groups()

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
                    temp_list += self.cells[y_index + 3 * off_set][x_index :x_index + 3]
                self.squares.append(Group(temp_list))  # TODO nice list comprhension for this?
                self._square_dict.update({(off_set, row_offset): self.squares[-1]})
                row_offset += 1

    def solve_puzzle(self) :
        """
        iterate through groups updating cells; when cell takes value, updata groups
        do while puzzle not solved. Will need to update process for handling guessing
        """
        debug_count = 1
        puzzle_updated = True #TODO change how failure to update is handled
        while self.update_number != 0 and puzzle_updated:  # TODO doesn't handle guessing; or invalid puzzle
            debug_count += 1
            puzzle_updated = False
            for row_num in range(9):
                for col_num in range(9):
                    cell_updates = self._check_updates(row_num, col_num)
                    puzzle_updated = puzzle_updated or (not cell_updates == {cell_status.no_change})
                    if cell_status.value_set in cell_updates:
                        self._update_groups(row_num, col_num)
                    if cell_status.puzzle_error_found in cell_updates:
                        self.print_puzzle()
                        print('\nerror found')
                        print(f'(row_num, col_num) == {(row_num, col_num)}')
                        input('break') #TODO need to better handle this flag
            if debug_count > 500:
                print('timeout')
                return False
            #input('break ')

    def _check_updates(self, row_num, col_num):
        cell, ret = self.cells[row_num][col_num], set()
        ret.add(cell.update_options(self.rows[row_num]))
        ret.add(cell.update_options(self.columns[col_num]))
        ret.add(cell.update_options(self._square_dict[(int(row_num/3), int(col_num/3))]))
        return ret

    def _update_groups(self, row_num, col_num):
        cell = self.cells[row_num][col_num]
        self.update_number -= 1
        self.rows[row_num].update_options(cell.val)
        self.columns[col_num].update_options(cell.val)
        self._square_dict[(int(row_num / 3), int(col_num / 3))].update_options(cell.val)

    def print_puzzle(self):
        for index, row in enumerate(self.cells):
            temp_str = ''.join([c.val for c in row])
            temp_line = '|'.join(a + b + c for a, b, c in zip(temp_str[::3], temp_str[1::3], temp_str[2::3]))
            print(' '.join(temp_line))
            if index in {2, 5}:
                print('-  ' * 8)
