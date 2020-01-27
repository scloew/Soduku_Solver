from ._contants import cell_status


class Group:

    def __init__(self, cells_list):
        self.cells = cells_list
        self.options = {str(i) for i in range(1, 10)} - {c.val for c in self.cells if c}

    def update_options(self, val): #TODO remove square debug
        #todo, will need to check for invalid puzzle here
        #if val not in self.options:
        #    return cell_status.puzzle_error_found
        self.options.remove(val)
