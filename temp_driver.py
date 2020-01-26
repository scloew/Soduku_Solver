from classes.puzzle import Puzzle


# def test_row_update():
#     print('\n*****\nChecking against row\n*****\n')
#     file = r'test_input\test_row_update.txt'
#     p = Puzzle(file)
#     print('original puzzle\n')
#     p.print_puzzle()
#     print()
#     cell = p.cells[0][0]
#     print(f'test group 1.row = {[c.val for c in p.rows[0].cells]}\n')
#     cell.update_options(p.rows[0])
#     new_group = p.columns[0]
#     print(f'test group 1.column = {[c.val for c in new_group.cells]}\n')
#     cell.update_options(new_group)
#     print('\nupdated puzzle\n')
#     p.print_puzzle()
#
#
# def test_column_update():
#     print('\n*****\nChecking against column\n*****\n')
#     file = r'test_input\test_column_update.txt'
#     p_new = Puzzle(file)
#     print('original puzzle\n')
#     p_new.print_puzzle()
#     print()
#     cell = p_new.cells[0][0]
#     print(f'test group 2.row = {[c.val for c in p_new.rows[0].cells]}\n')
#     cell.update_options(p_new.rows[0])
#     new_group = p_new.columns[0]
#     print(f'test group 2.column = {[c.val for c in new_group.cells]}\n')
#     cell.update_options(new_group)
#     print('\nupdated puzzle\n')
#     p_new.print_puzzle()
#
#
# def test_square_update():
#     print('\n*****\nChecking against squares\n*****\n')
#     file = r'test_input\test_square_update.txt'
#     p_newer = Puzzle(file)
#     print()
#     print('original puzzle\n')
#     p_newer.print_puzzle()
#     cell = p_newer.cells[1][1]
#     new_group = p_newer.squares[0]
#     print(f'test group 3.square = {[c.val for c in new_group.cells]}')
#     cell.update_options(new_group)
#     print('\nupdated puzzle\n')
#     p_newer.print_puzzle()
#
#
# def test_multi_group_update():
#     print('\n*****\nChecking update requiring row, column, and square\n*****\n') #TODO, this is the wrong way to do;
#                                                                                  #TODO start using pytest
#     file = r'test_input\test_row_column_update.txt'
#     multi_check_puzzle = Puzzle(file)
#     print()
#     print('original puzzle\n')
#     multi_check_puzzle.print_puzzle()
#     cell = multi_check_puzzle.cells[4][4]
#     row_group = multi_check_puzzle.rows[4]
#     column_group = multi_check_puzzle.columns[4]
#     square_group = multi_check_puzzle.squares[4]
#     print(f'test group 3.row = {[c.val for c in row_group.cells]}')
#     print(f'test group 3.column = {[c.val for c in column_group.cells]}')
#     print(f'test group 3.square = {[c.val for c in square_group.cells]}')
#     print('\n*****\n\n')
#     print(f'original cell options= {cell.options}; cell.val= {cell.val}')
#     cell.update_options(row_group)
#     print(f'after row update cell options= {cell.options}; cell.val= {cell.val}')
#     cell.update_options(column_group)
#     print(f'original column update cell options= {cell.options}; cell.val = {cell.val}')
#     cell.update_options(square_group)
#     print(f'original square update cell options= {cell.options}; cell.val = {cell.val}')
#     print('\nupdated puzzle\n')
#     multi_check_puzzle.print_puzzle()


def test_easy_puzzle(puzzle_file):
    print('\n*****\nChecking against easy puzzle\n*****\n')
    test_puzzle = Puzzle(puzzle_file)
    test_puzzle.print_puzzle()
    print('\n%%%%\n%%%%\n')
    test_puzzle.solve_puzzle()
    test_puzzle.print_puzzle()


def test_easy_puzzles():
    test_easy_puzzle(r'test_input\easy_puzzle.txt')
    test_easy_puzzle(r'test_input\easy_2.txt')


if __name__ == '__main__':
    #test_row_update()
    #test_column_update()
    #test_square_update()
    #test_multi_group_update()
    test_easy_puzzles()
