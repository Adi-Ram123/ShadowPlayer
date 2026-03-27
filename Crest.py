class Crest:
    def __init__(self, name, count, isFaith):
        self.name = name
        self.count = count
        self.isFaith = isFaith

    def update(self, offset: int):
        self.count += offset
