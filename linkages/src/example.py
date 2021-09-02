class Foo:

    def __init__(self, x):
        assert type(x) is int
        self.x = x

    def is_positive(self):
        return self.x > 0

    def get_tens(self):
        return self.x % 10


