from ._contants import status


class Group:

    def __init__(self, cells_list):
        self.cells = cells_list
        self.options = {str(i) for i in range(1, 10)} - {c.val for c in self.cells if c}

    def update_options(self, val):
        try:
            self.options.remove(val)
            return status.group_updated
        except KeyError:
            return status.puzzle_error_found
