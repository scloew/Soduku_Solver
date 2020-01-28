from .puzzle import Puzzle


def build_puzzle(puzzle_file):
    """
    parse puzzle_file, build a 2D list with list[i] being ith row
    and index list[i][j] being the value of cell (i, j)
    and initialize and return new puzzle with that list
    :param puzzle_file:
    :return: Puzzle
    """
    with open(puzzle_file, 'r') as in_file:
        cells = [[v for v in line if v != '\n'] for line in in_file.readlines()]
    return Puzzle(cells)
