from classes.puzzle import Puzzle

#file = r'test_input\test_2.txt'
file = r'test_input\test_3.txt' #Note this is a puzzle used to check cell will take value when only 1 option
p = Puzzle(file)
p.print_puzzle()
#sleep(2)
cell = p.cells[0][0]
#help(cell)
cell.update_options(p.cells[0])
new_group = [p.cells[i][0] for i in range(9)]
cell.update_options(new_group)

