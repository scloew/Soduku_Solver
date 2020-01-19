class Cell:

    def __init__(self, value=None):
        self.val = value
        self.options = {str(i) for i in range(1, 10)}

    def update_options(self, group):
        self.options -= {c.val for c in group if c.val}
        if len(self.options) == 1:
            self.val = self.options.pop()
            self.options = None
        print(self.options)
        print(f'cell value = {self.val}')
