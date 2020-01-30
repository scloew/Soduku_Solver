from ._contants import status


class Group:

    def __init__(self, cells_list):
        self.cells = cells_list
        self.options = {str(i) for i in range(1, 10)} - {c.val for c in self.cells if c}

    def update_options(self, val): #TODO remove square debug
        #todo, will need to check for invalid puzzle here
        #if val not in self.options:
        #    return status.puzzle_error_found
        try:
            self.options.remove(val)
            return status.group_updated
        except KeyError:
            return status.puzzle_error_found
