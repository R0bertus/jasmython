import jasmython as jasmine
from browser import window
expect = window.expect

def setup(objects):
    [o.group(o.suites[i]) for i, o in enumerate(objects)]

class Pizza(jasmine.Suite):
    def __init__(self, name="General suite", slices=1):
        super().__init__(name)
        self.initial_slices = slices
        self.slices = slices
        self.suites = [
            self.suite_1,
            self.suite_2
        ]

    def reset(self):
        self.slices = self.initial_slices

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
            print("Yummy in my Tummy!", self.get_slices())

        expect(self.get_slices()).toBe(0)

    def suite_1(self):
        self.test("My pizza should have at least 1 slice", self.i_can_eat_a_slice)
        self.test("My pizza has no slices left", self.i_cannot_eat_anymore_slices)
        self.test("My pizza does not reset, i'm hungry bro", self.i_cannot_eat_anymore_slices)

    def suite_2(self):
        self.suite("Nested Suite", Pizza(slices=25).suite_1)
        self.before_each(self.reset)
        self.test("My pizza has no slices left", self.i_cannot_eat_anymore_slices)
        self.test("My pizza should have at least 1 slice", self.i_can_eat_a_slice)
        self.test("My pizza resets, going to eat it all!", self.i_cannot_eat_anymore_slices)


if __name__ == '__main__':
    setup([
        Pizza("Pizza Salami", slices=3),
        Pizza("Pizza BBQ", slices=6)
    ])

