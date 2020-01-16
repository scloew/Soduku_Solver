class Cell:

    def __init__(self, value=None):
        self.val = value
        self.options = set(range(1,10))

    def update_options(self, group):
        self.options-= {c.val for c in group if c.val}
        print(self.options)

