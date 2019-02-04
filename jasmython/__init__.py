from browser import window
describe = window.describe
test = window.jasmine.getEnv().it
before_each = window.jasmine.getEnv().beforeEach


class Suite(object):
    def __init__(self, name):
        self.name = name

    def group(self, fnc):
        describe(self.name, fnc)

    def test(self, name, callback):
        test(name, callback)

    def suite(self, name, fnc):
        describe(name, fnc)

    def before_each(self, callback):
        before_each(callback)
