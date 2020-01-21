from classes.puzzle import Puzzle

print('\n*****\nChecking against row\n*****\n')
file = r'test_input\test_row_update.txt'
p = Puzzle(file)
print('original puzzle\n')
p.print_puzzle()
print()
cell = p.cells[0][0]
print(f'test group 1.row = {[c.val for c in p.rows[0].cells]}\n')
cell.update_options(p.rows[0])
new_group = p.columns[0]
print(f'test group 1.column = {[c.val for c in new_group.cells]}\n')
cell.update_options(new_group)
print('updated puzzle\n')
p.print_puzzle()

print('\n*****\nChecking against column\n*****\n')
file = r'test_input\test_column_update.txt'
p_new = Puzzle(file)
print('original puzzle\n')
p_new.print_puzzle()
print()
cell = p_new.cells[0][0]
print(f'test group 2.row = {[c.val for c in p_new.rows[0].cells]}\n')
cell.update_options(p_new.rows[0])
new_group = p_new.columns[0]
print(f'test group 2.column = {[c.val for c in new_group.cells]}\n')
cell.update_options(new_group)
print('updated puzzle\n')
p_new.print_puzzle()

print('\n*****\nChecking against squares\n*****\n')
file = r'test_input\test_square_update.txt'
p_newer = Puzzle(file)
print()
print('original puzzle\n')
p_newer.print_puzzle()
cell = p_newer.cells[1][1]
new_group = p_newer.squares[0]
print(f'test group 3.square = {[c.val for c in new_group.cells]}') #TODO this group failing
cell.update_options(new_group)
print('updated puzzle\n')
p_newer.print_puzzle() #TODO ummm..... why is puzzle changing - top left cell changing value??????
