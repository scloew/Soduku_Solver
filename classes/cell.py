from ._contants import status


class Cell:
    """represents one of the 81 entries in soduku puzzle"""
    def __init__(self, value):
        self.val = value
        self.options = None if value != '0' else {str(i) for i in range(1, 10)}
        self.ret_values = {
            0: status.puzzle_error_found,
            1: lambda: self.set_val(),
        } #TODO remove if unnecessary

    def update_options(self, group_options):
        # if self.options is None or self.options==self.options.intersection(group_options):
        #     return status.no_change
        # self.options = self.options.intersection(group_options)
        # return self.ret_values.get(len(self.options), status.options_update) #TODO why is this so slow???

        if self.options is None:
            return status.no_change  # TODO Ugly safety check to avoid intersection with None
        new_options = self.options.intersection(group_options)
        if len(new_options) == 1:
            self.set_val(new_options.pop())
            return status.value_set
        elif new_options == set():
            return status.puzzle_error_found
        elif new_options == self.options:
            return status.no_change
        else:
            self.options = new_options
            return status.options_update

    def set_val(self, val = None):
        self.val, self.options = (self.options.pop() if not val else val, None)
        return status.value_set

