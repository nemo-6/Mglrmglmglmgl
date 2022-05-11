class Price:
    def __init__(self, value, source):
        self.value = value
        self.source = source

    def __gt__(self, other):
        return self.value > int(other)

    def __lt__(self, other):
        return self.value < int(other)

    def __int__(self):
        return self.value
