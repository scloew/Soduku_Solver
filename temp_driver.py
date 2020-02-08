from classes.puzzle import Puzzle
from classes.puzzle_factory import build_puzzle


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
    file = r'test_input\test_easy_guess.txt'
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
    p_original = build_puzzle(r'test_input\test_easy_guess.txt')
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
    test_easy_puzzles()
    test_puzzle_update_trigger()
    test_invalid_puzzle()
    test_instantiate_by_puzzle()
    test_guessing()
    test_hard_puzzle()
