from classes.puzzle import Puzzle
from classes.puzzle_factory import build_puzzle


def test_row_update():
    print('\n*****\nChecking against row\n*****\n')
    file = r'test_input\test_row_update.txt'
    p = build_puzzle(file)
    print('original puzzle\n')
    p.print_puzzle()
    print()
    cell = p.cells[0][0]
    print(f'test group 1.row = {[c.val for c in p.rows[0].cells]}\n')
    cell.update_options(p.rows[0])
    new_group = p.columns[0]
    print(f'test group 1.column = {[c.val for c in new_group.cells]}\n')
    cell.update_options(new_group)
    print('\nupdated puzzle\n')
    p.print_puzzle()


def test_column_update():
    print('\n*****\nChecking against column\n*****\n')
    file = r'test_input\test_column_update.txt'
    p = build_puzzle(file)
    print('original puzzle\n')
    p.print_puzzle()
    print()
    cell = p.cells[0][0]
    print(f'test group 2.row = {[c.val for c in p.rows[0].cells]}\n')
    cell.update_options(p.rows[0])
    new_group = p.columns[0]
    print(f'test group 2.column = {[c.val for c in new_group.cells]}\n')
    cell.update_options(new_group)
    print('\nupdated puzzle\n')
    p.print_puzzle()


def test_square_update():
    print('\n*****\nChecking against squares\n*****\n')
    file = r'test_input\test_square_update.txt'
    p = build_puzzle(file)
    print()
    print('original puzzle\n')
    p.print_puzzle()
    cell = p.cells[1][1]
    new_group = p.squares[0]
    print(f'test group 3.square = {[c.val for c in new_group.cells]}')
    cell.update_options(new_group)
    print('\nupdated puzzle\n')
    p.print_puzzle()


def test_multi_group_update():
    print('\n*****\nChecking update requiring row, column, and square\n*****\n')
    file = r'test_input\test_row_column_update.txt'
    multi_check_puzzle = build_puzzle(file)
    print('\noriginal puzzle\n')
    multi_check_puzzle.print_puzzle()
    cell = multi_check_puzzle.cells[4][4]
    row_group = multi_check_puzzle.rows[4]
    column_group = multi_check_puzzle.columns[4]
    square_group = multi_check_puzzle.squares[4]
    print(f'test group 3.row = {[c.val for c in row_group.cells]}')
    print(f'test group 3.column = {[c.val for c in column_group.cells]}')
    print(f'test group 3.square = {[c.val for c in square_group.cells]}')
    print('\n*****\n\n')
    print(f'original cell options= {cell.options}; cell.val= {cell.val}')
    cell.update_options(row_group)
    print(f'after row update cell options= {cell.options}; cell.val= {cell.val}')
    cell.update_options(column_group)
    print(f'original column update cell options= {cell.options}; cell.val = {cell.val}')
    cell.update_options(square_group)
    print(f'original square update cell options= {cell.options}; cell.val = {cell.val}')
    print('\nupdated puzzle\n')
    multi_check_puzzle.print_puzzle()


def test_easy_puzzle(puzzle_file):
    print('\n*****\nChecking against easy puzzle\n*****\n')
    test_puzzle = build_puzzle(puzzle_file)
    test_puzzle.print_puzzle()
    print('\n%%%%\nsolved puzzle\n%%%%\n')
    test_puzzle.solve_puzzle()
    test_puzzle.print_puzzle()


def test_easy_puzzles():
    test_easy_puzzle(r'test_input\easy_puzzle.txt')
    test_easy_puzzle(r'test_input\easy_2.txt')


def test_puzzle_update_trigger():
    print('\n*****\nChecking failure to update trigger\n*****\n')
    file = r'test_input\test_row_update.txt'
    p = build_puzzle(file)
    print('original puzzle\n')
    p.print_puzzle()
    print()
    p.solve_puzzle()
    p.print_puzzle()


def test_invalid_puzzle():
    test_invalid_by_cell()
    test_invalid_by_group()


def test_invalid_by_cell():
    print('\n*****\nChecking invalid puzzle by cell is caught\n*****\n')
    file = r'test_input\test_invalid_puzzle.txt'
    p = build_puzzle(file)
    is_invalid = p.solve_puzzle()
    print(f'Puzzle valid = {is_invalid}')


def test_invalid_by_group():
    print('\n*****\nChecking invalid puzzle by group is caught\n*****\n')
    p = build_puzzle(r'test_input\test_invalid_by_group.txt')
    p.print_puzzle()
    print('\n%%%%\nafter attempted solve puzzle\n%%%%\n')
    is_invalid = p.solve_puzzle()
    print(f'Puzzle valid = {is_invalid}')
    p.print_puzzle()


def test_instantiate_by_puzzle():
    print('\n*****\nChecking instantiating puzzle with a puzzle\n*****\n')
    p_original = build_puzzle(r'test_input\easy_puzzle.txt')
    p_original.print_puzzle()
    print('original puzzle\n')
    p_copy = Puzzle([[c.val for c in row] for row in p_original.cells])
    print('new puzzle\n')
    p_copy.print_puzzle()


def test_guessing():
    test_guess(r'test_input\test_easy_guess_2.txt')
    test_guess(r'test_input\test_guess_blank_puzzle.txt')


def test_guess(file_name):
    print('\n*****\nChecking guessing\n*****\n')
    p = build_puzzle(file_name)
    p.print_puzzle()
    print('\n%%%%\nafter attempted solve puzzle\n%%%%\n')
    p.solve_puzzle()
    p.print_puzzle()


def test_hard_puzzle():
    p = build_puzzle(r'test_input\test_hard_puzzle.txt')
    print('\n*****\nChecking hard puzzle\n*****\n')
    print('original puzzle\n')
    p.print_puzzle()
    p.solve_puzzle()
    print('solved puzzle\n')
    p.print_puzzle()


if __name__ == '__main__':
    test_row_update()
    test_column_update()
    test_square_update()
    test_multi_group_update()
    test_easy_puzzles()
    test_puzzle_update_trigger()
    test_invalid_puzzle()
    test_instantiate_by_puzzle()
    test_guessing()
    test_hard_puzzle()
