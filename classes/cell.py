from ._contants import cell_status


class Cell:

    def __init__(self, value):
        self.val = value
        self.options = set() if value != '0' else {str(i) for i in range(1, 10)} #TODO is the == 0 necessary?

    def update_options(self, group):
        if not self.options or self.options == group.options:
            return cell_status.no_change #TODO Ugly safety check to avoid intersection with None
        new_options = self.options.intersection(group.options)
        if len(new_options) == 1:
            self.val = new_options.pop()
            self.options = None
            return cell_status.value_set
        elif new_options == ():
            print('debug error found')
            return cell_status.puzzle_error_found
        else:
            self.options = new_options
            return cell_status.options_update #TODO don't love repeated return statement in this case

