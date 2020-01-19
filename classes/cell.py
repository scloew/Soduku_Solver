class Cell:

    def __init__(self, value=None):
        self.val = value
        self.options = set() if self.val == 0 else {str(i) for i in range(1, 10)}

    def update_options(self, group):
        if self.options is None:
            return False
        self.options -= {c.val for c in group if c.val}
        if len(self.options) == 1:
            self.val = self.options.pop()
            self.options = None
            return True
        #print(self.options) #TODO remove print statemnts, or wrap in debug flas
        print(f'cell value = {self.val}')
        return False #TODO don't love duplicate return statement in this case
                     #TODO do I want puzzle to check if cell needs to be updated -> think so
