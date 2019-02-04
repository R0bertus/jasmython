from browser import window

describe = window.describe
expect = window.expect
it = window.it


class Suite(object):
    def __init__(self, name):
        self.name = name
        self.suite = describe(self.name)

    def add_test(self, name, callback):
        self.suite(self.name, it(name, callback))
