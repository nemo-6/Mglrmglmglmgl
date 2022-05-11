class Price:
    def __init__(self, value, source):
        self.value = value
        self.source = source

    def __gt__(self, other):
        if self.value is None:
            return True
        return self.value > other

    def __lt__(self, other):
        if self.value is None:
            return False
        return self.value < other

    def __mul__(self, other):
        if self.value is None:
            return 0
        return Price(self.value * other, self.source)

    def __add__(self, other):
        if self.value is None:
            return Price(other, self.source)
        return Price(self.value * other, self.source)

    def __iadd__(self, other):
        self.value += other
        return self

    def __int__(self):
        return self.value
