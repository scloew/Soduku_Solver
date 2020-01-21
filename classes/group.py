class Group:

    def __init__(self, cells_list):
        self.cells = cells_list
        self.options = {str(i) for i in range(1, 10)} - {c.val for c in self.cells if c}

    def print_options(self):
        print(self.options)

    def update_options(self):
        raise NotImplementedError #TODO need to implement this for after cell takes value, need to update options

    #TODO need update cells, options
