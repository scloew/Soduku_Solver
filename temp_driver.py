from classes.puzzle import Puzzle
from time import sleep

file = r'test_input\test_2.txt'
p = Puzzle(file)
p.print_puzzle()
#sleep(2)
cell = p.cells[0][0]
#help(cell)
cell.update_options(p.cells[0])
new_group = [p.cells[i][0] for i in range(9)]
cell.update_options(new_group)
