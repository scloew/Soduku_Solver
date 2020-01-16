class Cell:

    def __init__(self, value=None):
        self.val = value
        self.options = [None for _ in range(9)]

    def update_options(self, group):
        options = list(range(1,10))
        for cell in group:
            if cell.val:
                options[cell.val] = False

        self.options = [i for i in options if i]
        print(self.options)

