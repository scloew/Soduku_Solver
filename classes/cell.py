class Cell:

    def __init__(self, value=None):
        self.val = value
        self.options = [None for _ in range(10)] if not value else []

    def update_options(self, group):
        options = list(range(10))
        for cell in group:
            try:
                if cell.val:
                    options[cell.val] = False
            except Exception as e:
                print(e)
                print(cell.val)
                return

        self.options = [i for i in options if i]
        print(self.options)

