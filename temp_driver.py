from classes.puzzle import Puzzle

#file = r'test_input\test_2.txt'
#file = r'test_input\test_update_cell_val_invalidPuzzle.txt' #Note this is a puzzle used to check cell will take value when only 1 option
file = r'test_input\test_row_update.txt'
p = Puzzle(file)
p.print_puzzle()
cell = p.cells[0][0]
print(f'test group 1.row = {[c.val for c in p.cells[0]]}')
cell.update_options(p.cells[0])
new_group = [p.cells[i][0] for i in range(9)]
print(f'test group 1.column = {[c.val for c in new_group]}')
cell.update_options(new_group)
p.print_puzzle()

print('\n*****\nChecking against column\n*****\n')
file = r'test_input\test_column_update.txt'
p_new = Puzzle(file)
p_new.print_puzzle()
cell = p_new.cells[0][0]
print(f'test group 2.row = {[c.val for c in p_new.cells[0]]}')
cell.update_options(p_new.cells[0])
new_group = [p_new.cells[i][0] for i in range(9)]
print(f'test group 2.column = {[c.val for c in new_group]}') #TODO this group failing
cell.update_options(new_group)
p_new.print_puzzle()

print('\n*****\nChecking against column\n*****\n')
file = r'test_input\test_building_squares.txt'
p_newer = Puzzle(file)
p_newer.print_puzzle()
cell = p_newer.cells[0][0]
print(f'test group 2.row = {[c.val for c in p_newer.cells[0]]}')
cell.update_options(p_newer.cells[0])
new_group = [p_newer.cells[i][0] for i in range(9)]
print(f'test group 2.column = {[c.val for c in new_group]}') #TODO this group failing
cell.update_options(new_group)
p_newer.print_puzzle()
