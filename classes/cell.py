class Cell:

    def __init__(self, value):
        self.val = value
        self.options = set() if value != '0' else {str(i) for i in range(1, 10)} #TODO is the == 0 necessary?

    def update_options(self, group):
        self.options = self.options.intersection(group.options)
        if len(self.options) == 1:
            self.val = self.options.pop()
            self.options = set()
            return True
        return False #TODO don't love duplicate return statement in this case
                     #TODO do I want puzzle to check if cell needs to be updated -> think so
