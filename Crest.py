class Crest:
    def __init__(self, name, count, isFaith):
        self.name = name
        self.count = count
        self.isFaith = isFaith

    def update(self, offset: int):
        self.count += offset

    def __str__(self):
        return f"{self.name} ({self.count})"
