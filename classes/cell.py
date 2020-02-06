from ._contants import status


class Cell:
    """represents one of the 81 entries in soduku puzzle"""
    def __init__(self, value):
        self.val = value
        self.options = None if value != '0' else {str(i) for i in range(1, 10)}

    def update_options(self, group):
        if self.options is None:
            return status.no_change #TODO Ugly safety check to avoid intersection with None
        new_options = self.options.intersection(group.options)
        if len(new_options) == 1:
            self.set_val(new_options.pop())
            return status.value_set
        elif new_options == set():
            return status.puzzle_error_found
        elif new_options == self.options:
            return status.no_change #TODO this shouldn't be necessary; should be covered by the first if
        else:
            self.options = new_options
            return status.options_update

    def set_val(self, val):
        self.val = val
        self.options = None

