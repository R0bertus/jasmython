import jasmython as jasmine
from browser import window
expect = window.expect
test = window.jasmine.getEnv().it


class Pizza(jasmine.Suite):
    def __init__(self, name=None, fnc=None, slices=1):
        super().__init__(name, fnc)
        self.slices = slices

    def get_slices(self):
        return self.slices

    def eat_a_slice(self):
        if 0 < self.slices:
            self.slices -= 1
            return True
        else:
            return False

    def i_can_eat_a_slice(self):
        expect(self.get_slices()).toBeGreaterThan(0)

    def i_cannot_eat_anymore_slices(self):
        while self.eat_a_slice():
            pass

        expect(self.get_slices()).toBe(0)


def main():
    pizza = Pizza()
    test("My pizza should have at least 1 slice", pizza.i_can_eat_a_slice)
    test("My Pizza has no slices left", pizza.i_cannot_eat_anymore_slices)


if __name__ == '__main__':
    Pizza("Pizza Suite", main, 1)
