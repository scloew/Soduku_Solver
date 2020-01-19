class Group:

    def __init__(self):
        self.cells = [None for _ in range(9)]
        self.options = {str(i) for i in range(1, 10)}

    #TODO need update cells, options
