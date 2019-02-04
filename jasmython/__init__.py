from browser import window
describe = window.describe

class Suite(object):
    def __init__(self, name, fnc):
        if name is not None and fnc is not None:
            self.name = name
            self.suite = describe(self.name, fnc)


