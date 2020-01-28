from ._contants import cell_status


class Cell:

    def __init__(self, value):
        self.val = value
        self.options = None if value != '0' else {str(i) for i in range(1, 10)}

    def update_options(self, group): #TODO remove debug
        if self.options is None:
            return cell_status.no_change #TODO Ugly safety check to avoid intersection with None
        new_options = self.options.intersection(group.options)
        if len(new_options) == 1:
            self.val = new_options.pop()
            self.options = None
            return cell_status.value_set
        elif new_options == set():
            return cell_status.puzzle_error_found
        elif new_options == self.options:
            return cell_status.no_change #TODO this shouldn't be necessary; should be covered by the first if
        else:
            self.options = new_options
            return cell_status.options_update #TODO don't love repeated return statement in this case

